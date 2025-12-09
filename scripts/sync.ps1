$sourcePath = "ROOT:\SOURCE_FOLDER"
$dest = "https://STORAGE_ACCOUNT.file.core.windows.net/FILE_SHARE_NAME?SAS_KEY" #This can be put in .env too. sas key can be generated in Azure Storage account-> Security Networking ->Shared access signature

azcopy sync $sourcePath $dest --recursive=true
