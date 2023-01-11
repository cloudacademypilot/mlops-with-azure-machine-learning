param(
    [string]
    $Resourcegroupname
)

$WorkSpace = Get-AzResource -ResourceGroupName $Resourcegroupname -Resourcetype Microsoft.MachineLearningServices/workspaces
$WorkSpacename = $WorkSpace.Name

#Get azure access token
$token = (Get-AzAccessToken).Token

#Get subscription Id
$subscriptionUri = "https://management.azure.com/subscriptions?api-version=2020-01-01"
$headers1 = @{ Authorization = "Bearer $token"; 'ContentType' = "application/json"}
$res1 = Invoke-RestMethod -Method Get -ContentType "application/json" -Uri $subscriptionUri -Headers $headers1
$SubscriptionId = $res1.value[0].subscriptionId

#Get jobs
$endpointUri = "https://management.azure.com/subscriptions/"+$SubscriptionId+"/resourceGroups/"+$Resourcegroupname+"/providers/Microsoft.MachineLearningServices/workspaces/"+$WorkSpacename+"/jobs?api-version=2022-10-01"
$headers = @{ Authorization = "Bearer $token"; 'ContentType' = "application/json"}
$res2 = Invoke-RestMethod -Method Get -ContentType "application/json" -Uri $endpointUri -Headers $headers

$count = 0

foreach($i in $res2.value)
{
    foreach($j in $i)
    {
        $count=$count+1
        
    }
}

Write-Host $count

if($count -ge 4)
{
    Write-Host "Job is created"
}
else
{
    Write-Host "Job is not created"
}
