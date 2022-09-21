call venv\Scripts\activate.bat
del  build\*.*
pip3 freeze > requirements.txt
pip3 install -r requirements.txt --target build/
copy src\*.* build\
del build\*.dist-info
py -m zipapp build\ -p "/usr/bin/env python3" -o dist\mksubdir.pyz -c
