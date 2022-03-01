PowerShell -Command "Set-ExecutionPolicy Unrestricted" >> "%TEMP%\StartupLog.txt" 2>&1
Powershell -Command "Unblock-File .\installer.ps1"
PowerShell  -Command "Start-Process PowerShell -Verb RunAs  -WorkingDirectory (Get-Location)  -ArgumentList '-NoExit', 'cd %cd%; %cd%\installer.ps1 -user %USERNAME%'"  