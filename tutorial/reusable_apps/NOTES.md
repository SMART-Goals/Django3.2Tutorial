[REUSABLE APPS](https://docs.djangoproject.com/en/3.2/intro/reusable-apps/)

**What's in an App?**  
A Django application is a Python package that is specifically intended for use in a Django project.
An application may use common Django conventions, such as having models, tests, urls, and views submodules.

**MANIFEST.in File:**  
Only Python modules and packages are included in the package by default. To include additional files,
we’ll need to create a MANIFEST.in file.

**Package File:**  
Try building your package with python setup.py sdist (run from inside django-polls). This creates a directory
called dist and builds your new package, _django-polls-0.1.tar.gz_.

For more information on packaging, see Python’s Tutorial on
[Packaging and Distributing Projects](https://packaging.python.org/tutorials/packaging-projects/).

Installing the package:
```shell
python -m pip install --user django-polls/dist/django-polls-0.1.tar.gz
```