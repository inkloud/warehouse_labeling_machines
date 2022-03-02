# Installer with default settings. Use in Admin powershell
param ($user)

# install choco
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

#install mkcert
choco install mkcert

# create tls certificates
cd warehouse_labeling_machines
mkcert -install localhost 127.0.0.1
cd ..

# set correctly the project
.\python-3.9.4-embed-amd64\python.exe .\python-3.9.4-embed-amd64\get-pip.py

# create a start up script link
# put in the correct folder for launch application on start up
$curDir = Get-Location
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("C:\Users\$user\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\warehouse_labeling_machines_laucher.lnk")
$Shortcut.TargetPath = "$curdir\warehouse_labeling_machines\launcher.cmd"
$Shortcut.WorkingDirectory = "$curdir\warehouse_labeling_machines"
echo $Shortcut.WorkingDirectory
echo $Shortcut.TargetPath
$Shortcut.Save()
