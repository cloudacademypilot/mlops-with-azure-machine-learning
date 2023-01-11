param(
[string] $ResourceGroupName,
[string] $RawDataLakeAccountName
)
Write-Host "file upload script started"
 if ((Get-Module -ListAvailable Az.Accounts) -eq $null)
	{
       Install-Module -Name Az.Accounts -Force
    }

$uri = "https://raw.githubusercontent.com/CSALabsAutomation/mlops-with-azure-machine-learning/main/environments/env1/Artifacts/nyc-taxi-data.csv";
$bacpacFileName = "nyc-taxi-data.csv";

$StorageAccountKey = (Get-AzStorageAccountKey -ResourceGroupName $ResourceGroupName -Name $RawDataLakeAccountName)[0].Value;

$Ctx = New-AzStorageContext -StorageAccountName $RawDataLakeAccountName -StorageAccountKey $StorageAccountKey;

Invoke-WebRequest -Uri $uri -OutFile $bacpacFileName;
Set-AzStorageBlobContent -File $bacpacFileName -Container "azureml" -Blob 'nyc-taxi-data.csv' -Context $Ctx;
