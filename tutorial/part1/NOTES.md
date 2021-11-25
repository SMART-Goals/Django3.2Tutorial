[PART 1](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)

The very first step is to "create a project", which involves running a script that generates
the barebones set of directories and files.

Running:
```shell
django-admin startproject mysite
```
creates directory `mysite` with the barebones project.
```shell
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
- the top `mysite/` directory is just a container which can be renamed without breaking any code.
- the inner `mysite/` directory hosts the source code and it's a _python package_.
- `wsgi.py` is used by web servers to "put your project on the browser", that is, serve the web pages to
any browser making such requests. `asgi.py` has the same purpose, it's just another API.
  
**The Development Server:**
To start serving your App into the web browser on localhost:8008, type:
```shell
python manage.py runserver 8008
```
This server will automatically present in the browser any changes to your App, except when I add new files.

The top `mysite/` directory is a _Project_ which may be composed of one or more _Apps_. An _App_ is the
"unit of service", meaning it's designed to perform one and only one (high-level) task. The App has a
backend (models, views) and a user interface (templates). Apps are meant to be reusable.

I create App "polls" within `mysite` project:
```shell
python manage.py startapp polls
```
creates a `polls/` directory with the following structure:
```shell
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

At this point we need to add the top `mysite/` directory to the `$PYTHONPATH` variable, because we'll
routinely import our `poll` and `mysite` packages into python scripts.  

In Django we can associate all the presentation of a particular App to a root URL. For instance,
`http://127.0.0.1:8008/polls/` will be the root URL for all the pages presented by the `polls` App. This
is achieved by inserting statement
```python
path('polls/', include('polls.urls'))
```
in list `mysite.urls.urlpatterns`
