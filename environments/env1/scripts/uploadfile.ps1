param(
[string] $ResourceGroupName,
[string] $RawDataLakeAccountName
)
Write-Host "file upload script started"
 if ((Get-Module -ListAvailable Az.Accounts) -eq $null)
	{
       Install-Module -Name Az.Accounts -Force
    }

$uri = "https://raw.githubusercontent.com/CSALabsAutomation/mlops-with-azure-machine-learning/main/environments/env1/Artifacts/wine-quality-data.csv";
$bacpacFileName = "wine-quality-data.csv";

az account set --subscription "CS Labs Internal"

$StorageAccountKey = Get-AzStorageAccountKey -ResourceGroupName $ResourceGroupName -Name $RawDataLakeAccountName;

$Ctx = New-AzStorageContext -StorageAccountName $RawDataLakeAccountName -StorageAccountKey $StorageAccountKey.Value[0];

Invoke-WebRequest -Uri $uri -OutFile $bacpacFileName;
Set-AzStorageBlobContent -File $bacpacFileName -Container "raw" -Blob 'wine-quality-data.csv' -Context $Ctx;
