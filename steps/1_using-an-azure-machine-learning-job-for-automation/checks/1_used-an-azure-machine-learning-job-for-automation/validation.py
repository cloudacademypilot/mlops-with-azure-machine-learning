import json
import logging
import requests
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.subscription import SubscriptionClient

def handler():
    try:
        with open("steps/1_using-an-azure-machine-learning-job-for-automation/checks/1_used-an-azure-machine-learning-job-for-automation/params.json") as f:
            params = json.load(f)

        subscriptionId = params['subscription_id']
        rgName = params['resource_group_name']

        credential = AzureCliCredential()
        token = credential.get_token("https://management.azure.com").token

        headers = {
            'ContentType': 'application/json',
            'Authorization': f'Bearer {token}'
        }

        # Get ML Workspace name
        listWsUrl = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{rgName}/providers/Microsoft.MachineLearningServices/workspaces?api-version=2022-10-01'
        wsRes = requests.get(url=listWsUrl, headers=headers)
        workspaceName = ''
        if wsRes.status_code == 200:
            workspaces = wsRes.json()['value']
            if len(workspaces) != 0:
                workspaceName = workspaces[0]['name']

        # Get Data Assets
        listAssetsUrl = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{rgName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/data?api-version=2022-10-01'
        assetsRes = requests.get(url=listAssetsUrl, headers=headers)
        dataAssets = list()
        if assetsRes.status_code == 200:
            assets = assetsRes.json()['value']
            for asset in assets:
                dataAssets.append(asset['name'])
            if 'nyc-taxi-data' in dataAssets:
                print("Data asset created")
            else:
                print("Data asset not created")

        # Get Jobs
        listJobsUrl = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{rgName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/jobs?api-version=2022-10-01'
        jobsRes = requests.get(url=listJobsUrl, headers=headers)
        if jobsRes.status_code == 200:
            jobs = jobsRes.json()['value']
            if len(jobs) >= 1:
                print("Jobs created")
            else:
                print("Jobs not created")

        

    except Exception as e:
        logging.error(e)
        
if __name__=="__main__":
    handler()
