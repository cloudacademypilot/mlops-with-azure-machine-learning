import json
import logging
import requests
from azure.identity import AzureCliCredential

def handler():
    try:
        with open("steps/6_deploying-a-model-with-github-actions/checks/6_deployed-a-model-with-github-actions/params.json") as f:
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

        # Get endpoint
        endpoint = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{rgName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/onlineEndpoints?api-version=2022-10-01'
        end = requests.get(url=endpoint, headers=headers)
        if end.status_code == 200:
            endpoints = end.json()['value']

        if endpoints[0]['name'] and endpoints[0]['properties']['provisioningState'] == 'Succeeded':
            print('Endpoint is created')
        else:
            print('Endpoint is not created')

    except Exception as e:
        logging.error(e)
        
if __name__=="__main__":
    handler()
