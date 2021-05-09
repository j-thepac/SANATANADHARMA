# SANATANADHARMA

Git :

    There is 2 branches only
    main : connected to Heroku
    master : Working branch

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
