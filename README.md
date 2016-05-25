# learn-django

directory d3 contains an eclipse project.
It's a django project, so to run the django server from eclipse (PyDev mode) all that you have to do is select the project and chose Run->Run As->PyDev:Django

Naturally for this you need a mysql database server too.
I run one of these under Docker.

On OS/X this means you have to start a linux VM up.  (right? a docker container needs a LXC process group, which OS/X does not support, so kitematic runs a linux VM guest under VirtualBox)

I let Kitematic do the dirty work.

Start Kitematic.app and fire up a container that knows how to run mysql.
(note that the containers live inside the DOCKER_HOST virtual machine. you can ssh there using docker-machine ssh )

https://hub.docker.com/_/mysql/

I'm not really sure what i'm talking about here, but in the kitematic settings for my mysql container I see:
(I'm sure I set the password myself, but perhaps the version numbers came with the container)

MYSQL_MAJOR=5.7
MYSQL_VERSION=5.7.12-1debian8
MYSQL_ROOT_PASSWORD=my-secret-pw


What's going on here, I think, is that when the docker-host VM starts up the container it stuffs this env into the process running mysql. Then, in settings.py:

in the kitematic "configure ports" tab, I see:
3306 192.168.99.100:32768

This means that the port mysql listens to in the container is mapped to 32768 on my mac.

Hence, I set up Django:

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
(complicated enough plumbing alread)

once django is running (has passed its startup tests) it says:
http://127.0.0.1:8000/

look in url.py for the various URL's:

There is a really cool admin interface:
http://127.0.0.1:8000/admin

log in using account made by running manage.py

(I made the userid/password root/rootroot using an admin script manage.py. there is probably a way to do this in code too.. I've not looked into it: manage.py createsuperuser root )

http://127.0.0.1:8000/apipersons/
http://127.0.0.1:8000/apiperson/mathew




