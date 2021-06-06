# SANATANADHARMA


https://sanatanadharma.herokuapp.com/

Git :

    There is 2 branches only
    main : connected to Heroku
    master : Working branch

Heroku Db:

     db name :postgresql-objective-37602

     commands:

          heroku config -a sanatanadharma -s| grep DATABASE_URL
          heroku  pg:info -a sanatanadharma

Postgressql:

    $ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
    $ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    $ sudo apt-get update
    $ sudo apt-get install postgresql
    $sudo -u postgres createdb $USER
    $ psql # to start sql
    $\q # quit psql
    
SQlLite3 to Postgres:

    python manage.py dumpdata > db.json
    Change the database settings to new database such as of MySQL / PostgreSQL.

        DATABASES = {
        ‘default’: {
        ‘ENGINE’: ‘django.db.backends.postgresql_psycopg2’,
        ‘NAME’: ‘my_db’,
        ‘USER’ : ‘xxxx’,
        ‘PASSWORD’ : ‘xxxxx’,
        ‘HOST’ : ‘localhost’,
        ‘PORT’ : ‘5432’,
        }
        }
    python manage.py migrate
    python manage.py shell 
    Enter the following in the shell
    from django.contrib.contenttypes.models import ContentType
    ContentType.objects.all().delete()
    python manage.py loaddata db.json

Heroku :Spins up a container when u deploy

    Set to AutoDeploy
    logs :More > view logs 
    Procfile: Commands to run when container is spun up.
            “Procfile” without any file extension in your project root (top most)
              web: gunicorn projectname.wsgi --log-file -
    For python requirments.txt is auto run
    
    
Pre-Req:


    1.  Install python 3+
    2.  Use pycharm to create to Virtual Env automatically 
    3.  skip if you already created django
        a)  pip install virtualenv
        b)  virtualenv venv
        c)  source venv/bin/activate
    4.  Make sure u create a bashrc file has DJANGO_SECRET_KEY="key values" and DJANGO_DEBUG = "True" 


Files:

    procfile - used for Heroku
    
Steps :

    cd SANATANADHARMA/
    python manage.py runserver


DB :

    Using built in SQLLite3 as expected hits is not more than 100K

Other

    python -m django --version #check version
    django-admin    #all commands 



http://www.matrix.umcs.lublin.pl/DOC/python-django-doc/html/howto/deployment/checklist.html
https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
https://www.youtube.com/watch?v=tUqUdu0Sjyc&list=RDCMUCTZRcDjjkVajGL6wd76UnGg&start_radio=1&t=337

Resources :

1.  Heroku+Git :https://www.youtube.com/watch?v=Q_YOYNiSVDY
2.  Heroku+Git :https://studygyaan.com/django/django-everywhere-host-your-django-app-for-free-on-heroku
3.  https://www.youtube.com/watch?v=hu99aiU0tIA
