Microsoft Windows [Version 10.0.22000.493]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Ayo>pip install virtualenv
Collecting virtualenv
  Using cached virtualenv-20.14.1-py2.py3-none-any.whl (8.8 MB)
Collecting platformdirs<3,>=2
  Downloading platformdirs-2.5.2-py3-none-any.whl (14 kB)
Collecting filelock<4,>=3.2
  Downloading filelock-3.6.0-py3-none-any.whl (10.0 kB)
Collecting distlib<1,>=0.3.1
  Using cached distlib-0.3.4-py2.py3-none-any.whl (461 kB)
Collecting six<2,>=1.9.0
  Using cached six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: distlib, six, platformdirs, filelock, virtualenv
Successfully installed distlib-0.3.4 filelock-3.6.0 platformdirs-2.5.2 six-1.16.0 virtualenv-20.14.1

C:\Users\Ayo>vcd desktop
'vcd' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Ayo>cd desktop

C:\Users\Ayo\Desktop>pip install virtualenv
Requirement already satisfied: virtualenv in c:\users\ayo\appdata\local\programs\python\python310\lib\site-packages (20.14.1)
Requirement already satisfied: six<2,>=1.9.0 in c:\users\ayo\appdata\local\programs\python\python310\lib\site-packages (from virtualenv) (1.16.0)
Requirement already satisfied: filelock<4,>=3.2 in c:\users\ayo\appdata\local\programs\python\python310\lib\site-packages (from virtualenv) (3.6.0)
Requirement already satisfied: platformdirs<3,>=2 in c:\users\ayo\appdata\local\programs\python\python310\lib\site-packages (from virtualenv) (2.5.2)
Requirement already satisfied: distlib<1,>=0.3.1 in c:\users\ayo\appdata\local\programs\python\python310\lib\site-packages (from virtualenv) (0.3.4)

C:\Users\Ayo\Desktop>virtualenv env
created virtual environment CPython3.10.4.final.0-64 in 21233ms
  creator CPython3Windows(dest=C:\Users\Ayo\Desktop\env, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=C:\Users\Ayo\AppData\Local\pypa\virtualenv)
    added seed packages: pip==22.0.4, setuptools==62.1.0, wheel==0.37.1
  activators BashActivator,BatchActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator

C:\Users\Ayo\Desktop>env\Scripts\activate

(env) C:\Users\Ayo\Desktop>env\Scripts\deactivate
C:\Users\Ayo\Desktop>env\Scripts\activate

(env) C:\Users\Ayo\Desktop>pip install django
Collecting django
  Downloading Django-4.0.4-py3-none-any.whl (8.0 MB)
     ---------------------------------------- 8.0/8.0 MB 3.1 MB/s eta 0:00:00
Collecting asgiref<4,>=3.4.1
  Downloading asgiref-3.5.1-py3-none-any.whl (22 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Collecting tzdata
  Using cached tzdata-2022.1-py2.py3-none-any.whl (339 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.5.1 django-4.0.4 sqlparse-0.4.2 tzdata-2022.1

(env) C:\Users\Ayo\Desktop>django-admin

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    runserver
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver
Note that only Django core commands are listed as settings are not properly configured (error: Requested setting INSTALLED_APPS, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.).

(env) C:\Users\Ayo\Desktop>django-admin startproject studybud

(env) C:\Users\Ayo\Desktop>cd studybud

(env) C:\Users\Ayo\Desktop\studybud>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 03, 2022 - 17:43:20
Django version 4.0.4, using settings 'studybud.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[03/May/2022 17:43:36] "GET / HTTP/1.1" 200 10697
[03/May/2022 17:43:37] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[03/May/2022 17:43:38] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[03/May/2022 17:43:38] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
[03/May/2022 17:43:38] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
Not Found: /favicon.ico
[03/May/2022 17:43:39] "GET /favicon.ico HTTP/1.1" 404 2112
