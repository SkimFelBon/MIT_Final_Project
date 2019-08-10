# To select all tables from in db
c.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
# To print result
c.fetchall()


## TO START NEW FLASK VIRTUALENV IN POWERSHELL(win10) DO THIS
PS C:\> mkdir testFlask
PS C:\> cd testFlask
PS C:\testFlask> python -m virtualenv testFlaskENV
***
Installing setuptools, pip, wheel...
done...
***
PS C:\testFlask> Set-ExecutionPolicy unrestricted
PS C:\testFlask> . testFlaskENV\Scripts\activate
(testFlaskENV) PS C:\testFlask> Set-ExecutionPolicy restricted
(testFlaskENV) PS C:\testFlask> pip install flask
***
Installing collected packages: MarkupSafe, Jinja2, click, Werkzeug, itsdangerous, flask
Successfully installed Jinja2-2.10.1 MarkupSafe-1.1.1 Werkzeug-0.15.5 click-7.0 flask-1.1.1 itsdangerous-1.1.0
***
(testFlaskENV) PS C:\testFlask> $env:FLASK_ENV="development"
(testFlaskENV) PS C:\testFlask> flask run

 * Environment: development
 * Debug mode: on
 * Restarting with stat
c:\testflask\testflaskenv\scripts\python.exe: No module named C:\testFlask\testFlaskENV\Scripts\flask
(testFlaskENV) PS C:\MyPythonScripts\OSSU\testFlask>
OR
(testFlaskENV) PS C:\testFlask> python -m flask run
## DONE
