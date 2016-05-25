# learn-django repo contains django rest experiment

directory d3 contains an eclipse project.
It's a django project, so to run the django server from eclipse (PyDev mode) you select the project and chose Run->Run As->PyDev:Django

## mysql/Docker on OS/X
I wrote the example against mysql, do you need a mysql database server too.
I run one of these under Docker.

On OS/X this means you have to start a linux VM up.  (A docker container needs a LXC process group, which OS/X does not support, so kitematic runs a linux VM guest under VirtualBox)

Start Kitematic.app and fire up a container that knows how to run mysql.
For instance https://hub.docker.com/_/mysql/

(note that the containers live inside the DOCKER_HOST virtual machine. 
you can ssh there using docker-machine ssh )

I'm not really sure of the details here, but in the kitematic settings for my mysql container I see:
(I'm sure I set the password myself, but perhaps the other vars, like version numbers came with the container)

MYSQL_MAJOR=5.7
MYSQL_VERSION=5.7.12-1debian8
MYSQL_ROOT_PASSWORD=my-secret-pw

What's going on here, I think, is that when the docker-host VM starts up the container it stuffs this env into the process group running mysql. Then, in settings.py:

in the kitematic "configure ports" tab, I see:
3306 192.168.99.100:32768

This means that the port mysql listens to in the container/VM guest is mapped to 32768 on the host (my mac).

## Django app setup

Django has to know about the mysql server we set up above

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb', #created this by hand using mysql
        'PORT': '32768',
        'HOST': '192.168.99.100',
        'USER': 'root',
        "PASSWORD": "my-secret-pw"
    }
}

So django will connect onto the mysql instance inside the docker container inside the VMhost. 
(complicated enough plumbing already)

## running

look in url.py for the various URL's.

once django is running (has passed its startup tests) it prints a bunch of stuff on its console, including the URL

http://127.0.0.1:8000/


There is a really cool admin interface, whereby you can add, remove and edit objects:
http://127.0.0.1:8000/admin

NB You have to authenticate yourself to django to be allowed to run the admin interface.
(obviously.. you can change any model object!)

log in using account made by running manage.py

(I made the userid/password root/rootroot using an admin script manage.py. 
there is probably a way to do this in code too.. 
I've not looked into it: 

`manage.py createsuperuser root`

http://127.0.0.1:8000/apipersons/
http://127.0.0.1:8000/apiperson/mathew




