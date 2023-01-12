import json
import logging
import requests
from azure.identity import AzureCliCredential

def handler():
    try:
        with open("steps/5_working-with-environments-in-github-actions/checks/5_worked-with-environments-in-github-actions/params.json") as f:
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

        # Get Jobs
        listJobsUrl = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{rgName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/jobs?api-version=2022-10-01'
        jobsRes = requests.get(url=listJobsUrl, headers=headers)
        if jobsRes.status_code == 200:
            jobs = jobsRes.json()['value']
            if len(jobs) >= 4:
                print("Jobs created")
            else:
                print("Jobs not created")

    except Exception as e:
        logging.error(e)
        
if __name__=="__main__":
    handler()
