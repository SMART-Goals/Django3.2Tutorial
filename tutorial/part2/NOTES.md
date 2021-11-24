For this tutorial, database _SQLite_ is enough. However, if my future project is going to server many
users at any given time, it's better to start with a different database such as _PostgreSQL_. Note that
these other databases will require specifying `USER`, `PASSWORD`, and `HOST` in the _settings.py_ module.

I set the time zone to that of Oak Ridge (a.k.a New York)
```python
TIME_ZONE = 'America/New_York' TIME_ZONE = 'America/New_York'
```

Apps are plugged into my project by listing them in ``INSTALLED_APPS``. Some of the default Apps
(admin, auth, contenttypes, and sessions) define
models that require a database. Each of these models (python classes) is to be related to a table in
my database, and these tables _must_ be created. This creation process is referred to as _migration_:
```shell
python manage.py migrate
```

The default Apps have a backend for Models and Views, as well as templates that could be exposed in
my project's website.

After including the polls App in `INSTALLED_APPS`, we have to create the tables in the database. A first,
intermediate step is to create a more serialized versions of the model classes.
```shell
python manage.py makemigrations polls
```
The output is module `polls.migrations.0001_initial.py`. This module can be stored and tracked
in a _version control repository_. It can be translated into SQL language and printed to `stdout`:
```shell
python manage.py sqlmigrate polls 0001
```
The default table names are `polls_question` for model `Question`, and `polls_choice` for model `Choice`.
Avoid problems by having model names differing only in the case. If this is unavoidable, the default
table names can be tweaked.

The migrations module can now be incorporated into the database in a second step:
```shell
python manage.py migrate
```

**Django Python Interactive Interpreter:**  
This command sets environment variable `DJANGO_SETTINGS_MODULE` to `mysite.settings` and starts an
interactive python session
```shell
python manage.py shell
```

**Object Primary Key:**
The _Primary Key_ of an object saved in the database is its _id_. Attributes `id` and `pk` (for primary key)
thus have the same value.

**Relationships Among Models:**  
When defining a model class, we can reference other model classes as fields, declaring the arity
of the relationship
```python
from django.db import models
class Child(models.Model):
    # has only one favorite toy, and the toy can have only one owner, thus use OneToOneField
    fav_toy = models.ForeignKey(Toy, on_delete=models.CASCADE, primary_key=True)

    # has only one father, but the father can have more han one child. The
    # many-to-one relationship requires ForeignKey
    father = models.ForeignKey(Father, on_delete=models.CASCADE)

    # there's no specialized class for the one-to-many relationship. For instance a child
    # can have many crayons, and each crayon has only one owner. In this case we have to insert a
    # ForeignKey as class attribute of class Crayon, referencing a Child.

    # has many siblings, and each sibling has many siblings, thus use ManyToManyField.
    siblings = models.ManyToManyField(Sibling, on_delete=models.CASCADE)
```

**The admin Site:**  
The _admin_ app is plugged-in by default in every Django project. It allows power-users to edit content,
that is, modifying the state of the database.  
Let's create power-user "admin" with fake email admin@example.com and password "admin":  
```shell
python manage.py createsuperuser
```

The initial admin site (localhost:8008/admin/) only contains the list of users and groups which can be
edited thanks to the _auth_ App thas is also plugged-in by default in every Django project.  
More functionality can be included in the admin site, in this tutorial we'll allow the power-user to
modify the database of questions and choices. For this purpose, one only has to "register" the
models within module `mysite.admin`.
