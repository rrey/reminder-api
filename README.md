# What is the Reminder API ?

Let's say you an OPS, you deliver projects and:
* you have several environments for your project (dev, staging, etc ...)
* Each environment have several servers.
* Multiple software are running on the servers.
* Some of the software have an WUI, some have several.

If you match these asumptions you probably ask youself some of the following questions time to time:

* What is the URL of the admin WUI for <random soft name here> ?
* How many servers are in the <random soft name here> cluster ?
* What are the server names/addresses for the <random soft name here> servers ?

Because having every URLs in our browser and documents/tables with all the servers is
not an acceptable solution, the Reminder aims at centralizing all the information in a
database and offer an API allowing to add/update/retrieve/remove information.

Other components are available:
* reminder-wui: A web interface on top of the reminder-api allowing to easilly navigate
in the environments.
* ansible-module-reminder: An ansible module allowing to interact with reminder-api from
Ansible to populate the database while building an environment.

# Start the server

```
$ cd reminder_api
$ python manage.py makemigrations project
$ python manage.py makemigrations reminder
$ python manage.py makemigrations inventory
$ python manage.py migrate
$ python manage.py runserver
```

Enjoy the interface on 127.0.0.1:8000 (the browsable api too).
