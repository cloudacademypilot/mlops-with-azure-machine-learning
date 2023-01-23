param(
[string] $ResourceGroupName,
[string] $RawDataLakeAccountName
)
Write-Host "file upload script started"
 if ((Get-Module -ListAvailable Az.Accounts) -eq $null)
	{
       Install-Module -Name Az.Accounts -Force
    }

$uri = "https://mscalabshare.blob.core.windows.net/assets/mlops/data/nyc-taxi-data.csv?sp=r&st=2023-01-23T03:32:39Z&se=2099-01-23T11:32:39Z&spr=https&sv=2021-06-08&sr=b&sig=exHo%2B%2FKRnv%2BuBzSJAhbtzXgKL9aY69uctNfUi%2F5H3B8%3D";
$bacpacFileName = "nyc-taxi-data.csv";

$StorageAccountKey = (Get-AzStorageAccountKey -ResourceGroupName $ResourceGroupName -Name $RawDataLakeAccountName)[0].Value;

$Ctx = New-AzStorageContext -StorageAccountName $RawDataLakeAccountName -StorageAccountKey $StorageAccountKey;

Invoke-WebRequest -Uri $uri -OutFile $bacpacFileName;
Set-AzStorageBlobContent -File $bacpacFileName -Container "azureml" -Blob 'nyc-taxi-data.csv' -Context $Ctx;
