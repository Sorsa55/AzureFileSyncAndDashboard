# AzureFileSyncAndDashboard

Showcase!
Small File Sync for azure file share in storage account and dashboard for that aswell
This was my school work and kinda interesting setup
You need AzCopy for this

Sadly this has not much personal usecases since Azure is expensive to use(just for making this to work for 2-3 weeks ive used over 30$ from $200 free credit)
Regardless it was still interesting to setup.

How to use

1. Donwload AzCopy from https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10
2. Put its path into EnviorementalVariables path
3. Make storage account and inside that make fileshare
4. Download scripts. Scripts folder goes into root directory (For example for me its "C:/scripts"
5. then make also empty folder inside the root
6. in scripts use that empty folder as sourcepath
7. For destination you need storage account name and sas key. sas key can be generated in Azure storage account by going to security and networking and then Shared access signature
8. Then the link is "https://STORAGE_ACCOUNT.file.core.windows.net/FILE_SHARE_NAME?SAS_KEY" so you also need Storage account name and file share name
9. Then once you have this you should be able to use command: powershell -ExecutionPolicy Bypass -File "C:\Scripts\sync.ps1"

How to make it into autmatic syncronization

1. Open Task Scheduler and create new task
  ->For baisic settings it realy depends how you want them
2. In Triggers put it for example to scheduel everyday at 12🕧(or however you want it to be)
3. In action create new-> Start programm->"Programm/script" put Powershell.exe and in arguments put -ExecutionPolicy Bypass -File "C:\Scripts\sync.ps1"
4. now you have automatic syncronization
(NOTE! its not free to use, microsoft azure is kinda expensive)

For dashboard you can use the dashboard script BUT you need
Python and flask
File share name
Access key which can be found by going to security and networking and then access key.
Then you can either use it localy or upload it to VM.

Also there is atleast not yet no real frontend in dashboard just generic html stuff(was not priority at all)
