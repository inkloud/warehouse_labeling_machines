$file = Get-ChildItem ./ | Where{$_.LastWriteTime -gt (Get-Date).AddDays(-30) }  | Where {$_.Name -match '.pem'}

If($file -eq $null) {
    mkcert -install localhost 127.0.0.1
} Else {
    echo "CA already validate"
}

python -m venv .venv

$VenvPython = ".\.venv\Scripts\python.exe"
$VenvPip    = ".\.venv\Scripts\pip.exe"

# Aggiorna pip
& $VenvPython -m pip install --upgrade pip

# Installa dipendenze
& $VenvPip install -r .\requirements-lock.txt

# Variabili ambiente Flask
$Env:FLASK_APP = "web.py"
$Env:FLASK_DEBUG = 1

# Avvio app
& $VenvPython .\web.py 5001