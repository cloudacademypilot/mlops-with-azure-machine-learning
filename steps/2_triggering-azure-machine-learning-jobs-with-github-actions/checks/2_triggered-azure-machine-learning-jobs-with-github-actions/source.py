import json
import requests
from azure.identity import ClientSecretCredential, SharedTokenCacheCredential
from azure.mgmt.resource import ResourceManagementClient

def with_hint(result, hint=None):
    return {'result': result, 'hint_message': hint} if hint else result

def handler(event, context):
    credentials, subscriptionId = get_credentials(event)
    rgName = event['environment_params']['resource_group']

    bearer_token = credentials.get_token('https://management.azure.com/.default')

    headers = {
        'ContentType': 'application/json',
        'Authorization': f'Bearer {bearer_token.token}'
    }

    # Get ML Workspace name
    listWsUrl = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{rgName}/providers/Microsoft.MachineLearningServices/workspaces?api-version=2022-10-01'
    wsRes = requests.get(url=listWsUrl, headers=headers)
    workspaceName = None
    if wsRes.status_code == 200:
        workspaces = wsRes.json()['value']
        if len(workspaces) != 0:
            workspaceName = workspaces[0]['name']
    if not workspaceName:
        return with_hint(False, 'Azure Machine Learning workspace not found')

    # Get Jobs
    listJobsUrl = f'https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{rgName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/jobs?api-version=2022-10-01'
    jobsRes = requests.get(url=listJobsUrl, headers=headers)
    jobs = []
    if jobsRes.status_code == 200:
        jobs = jobsRes.json()['value']

    return with_hint(len(jobs) >= 2, 'Second Azure Machine Learning job not found')


def get_credentials(event):
    subscription_id = event['environment_params']['subscription_id']
    credentials = ClientSecretCredential(
        client_id=event['credentials']['credential_id'],
        client_secret=event['credentials']['credential_key'],
        tenant_id=event['environment_params']['tenant']
    )
    return credentials, subscription_id