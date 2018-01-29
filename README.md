[![Build Status](https://travis-ci.org/rrey/reminder-api.svg?branch=master)](https://travis-ci.org/rrey/reminder-api)

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

# Quick start

## Using Docker

```
$ docker pull rrey/reminder_api
$ docker run -it --rm -p 8000:8000 -d reminder_api
```

## From the sources

### Development server

```
$ make init
$ make run
```

Enjoy the interface on 127.0.0.1:8000 (the browsable api too).

### Docker

You can edit the Dockerfile and build your own image:

```
$ make dockerbuild
$ make dockerrun
```

The first command will build a Docker image based on the Docker file, the
second will start a container based on this image.

# Samples

## Project detail (ex : /projects/awesome/)

Returns a Project JSON representation:
```
{
    "id": 1,
    "name": "awesome",
    "environments": [
        {
            "id": 1,
            "name": "staging"
        }
    ]
}
```

## Environment detail (ex : /environments/1/)

Returns an Environment JSON representation:
```
{
    "project": 1,
    "id": 1,
    "name": "staging",
    "reminder": {
        "id": 1,
        "stacks": [
            {
                "id": 1,
                "name": "kafka",
                "urls": [
                    {
                        "url": "http://kafka-01.example.com/"
                    }
                ],
                "hosts": [
                    {
                        "hostname": "kafka-01.example.com"
                    }
                ]
            }
        ]
    },
    "inventory": {
        "id": 1
    }
}
```
