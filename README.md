dj-calsimple
=========

Simple PoC for Django-backed CalCentral "mashup" project
Currently includes a number of additional apps that will neeed to be trimmed
out (but that won't affect your experiments)

# Initial setup (first run only)

sudo easy_install pip   // If you don't have pip already
pip install virtualenvwrapper   // If you don't have virtualenv already
mkvirtualenv dj-calsimple
workon dj-calsimple
cdvirtualenv
git clone https://github.com/shacker/dj-calsimple.git
pip install -r requirements.txt

We put all of our own apps in the "apps" directory, so it needs to be on the virtualenv import path.
    cd path/to/apps
    pwd [copy]
    add2virtualenv [paste]

You'll need a local_settings.py containing the settings specific
to your machine. Get a starter version at:
https://github.com/shacker/djcc/wiki/Sample-local_settings.py
Edit that file to match your setup (see below on database options).

Now:
cp dj-calsimple/manage.py .

You can either start with an empty dataset, or use provided sample data.
Scot can provide sample data (request from shacker@berkeley.edu).
Place the sample data in dj-calsimple/dj-calsimple/data/all.json, then create initial tables with:

python manage.py syncdb

Create a superuser login for yourself if you know there's not going to be one
in the sample data you'll be loading:

python manage.py createsuperuser

Now load up the sample data:
python manage.py loaddata dj-calsimple/data/all.json

# Daily workflow:

workon dj-calsimple
cdvirtualenv
python manage.py runserver

visit: http://127.0.0.1:8000/
visit: http://127.0.0.1:8000/admin

git ignore:
    settings_local.py
    *.pyc


# Misc notes

Unlike OAE, the Django console should be run in the foreground, not background - it refreshes itself in seconds, and output is always visible.

Make sure mysql is set to create tables and fields as utf8. Running this query after db creation will ensure that all future tables and fields are set correctly by default:
ALTER DATABASE [dbname] CHARACTER SET utf8 COLLATE utf8_general_ci;

In the admin, create groups: students, staff, instructors

Load sample data by running create_users.py

Note: Django has its own "staff" status which just means a user has basic access to the admin. NOT that they can see anything in the admin you haven't OK'd. Not to be confused with them being staff of UCB.

To generate a graphical display of the models relationship:

Create a dot file
$ python manage.py graph_models -a > my_project.dot

Create a PNG image file called my_project_visualized.png with application grouping
$ python manage.py graph_models -a -g -o my_project_visualized.png

Create a dot file for only the 'foo' and 'bar' applications of your project
$ python manage.py graph_models foo bar > my_project.dot

Install Graphviz for Mac to view .dot files


Some 3rd party template systems (such as jQuery templates) use a template syntax similar to Django's. To prevent these from conflicting, I've installed a templatetag called "verbatim". If you need it, use:

{% load verbatim %}
...
{% verbatim %}
{% endverbatim %}

To start debugging, put this anywhere in your code and reload:

import pdb; pdb.set_trace()

See this for good info on pdb debugging:
http://ericholscher.com/blog/2008/aug/31/using-pdb-python-debugger-django-debugging-series-/

Notes:
use 'l' to list the current function
use 's' for step
use 'r' for return, to go to the end of functions
use "where" for a traceback showing how you got to that place in the code
use 'locals()' to see all local variables
use up + down to see parents and children (unclearl on this)
use keys 'c' or 'n' to continue or go to next.

