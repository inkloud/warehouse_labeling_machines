PowerShell -Command "Set-ExecutionPolicy Unrestricted" >> "%TEMP%\StartupLog.txt" 2>&1
Powershell -Command "Unblock-File .\launch_server.ps1"
PowerShell  -windowstyle hidden ".\launch_server.ps1" 
