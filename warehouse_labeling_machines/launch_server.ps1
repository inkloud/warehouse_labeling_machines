$file = Get-ChildItem ./ | Where{$_.LastWriteTime -gt (Get-Date).AddDays(-30) }  | Where {$_.Name -match '.pem'}

If($file -eq $null) {
    mkcert localhost
    mkcert -install
} Else {
    echo "CA already validate"
}
..\python-3.9.4-embed-amd64\Scripts\pip3 install -r .\requirements-lock.txt
$Env:FLASK_APP="web.py" 
$Env:FLASK_DEBUG=1
#flask run --host=0.0.0.0
..\python-3.9.4-embed-amd64\python.exe .\web.py 5001