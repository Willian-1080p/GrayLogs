No powershell como admin

Rode

Test-NetConnection 192.168.15.234 -Port 5044

se 
TcpTestSucceeded : True

Rode

cd C:\Winlogbeat\winlogbeat-7.17.15-windows-x86_64
powershell.exe -ExecutionPolicy Bypass -File .\install-service-winlogbeat.ps1
Start-Service winlogbeat
Get-Service winlogbeat
