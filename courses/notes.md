the following are key tricks for django project

1. django-admin startproject  <projectname>
2. django-admin startapp <appname>
3. python3 manage.py runserver #starts the server
4. python3 manage.py makemigrations #prepares the migration
5. python3 manage.py migrate  #implement migration
6. python3 manage.py dumpdata courses --indent=2
(dumpdata command dumps data from dabase into stdout, serialized in json format)
7. python3 manage.py loaddata subjects.json #loads data into database