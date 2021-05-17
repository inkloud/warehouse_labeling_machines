Get-ChildItem ./ | Where{$_.LastWriteTime -lt (Get-Date).AddDays(-3) }  | Where {$_.Name -match '.*parcel.*.pdf'} | ForEach-Object { Remove-Item -LiteralPath $_.Name }
#python3 -m venv ENV
#ENV\Scripts\activate
..\python-3.9.4-embed-amd64\Scripts\pip3 install -r .\requirements-lock.txt
$Env:FLASK_APP="web.py" 
$Env:FLASK_DEBUG=1
#flask run --host=0.0.0.0
..\python-3.9.4-embed-amd64\python.exe .\web.py 5001