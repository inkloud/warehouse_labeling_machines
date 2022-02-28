$file = Get-ChildItem ./ | Where{$_.LastWriteTime -lt (Get-Date).AddDays(-30) }  | Where {$_.Name -match '.key'}
If($file -eq $null) {
    echo "CA already in use"
} Else {
    mkcert localhost
    mkcert -install
}
..\python-3.9.4-embed-amd64\Scripts\pip3 install -r .\requirements-lock.txt
$Env:FLASK_APP="web.py" 
$Env:FLASK_DEBUG=1
#flask run --host=0.0.0.0
..\python-3.9.4-embed-amd64\python.exe .\web.py 5001