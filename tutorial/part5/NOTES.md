For full details on testing, see [Testing in Django](https://docs.djangoproject.com/en/3.2/topics/testing/).

**Testing and App:**  
To test App _polls_:
```shell
python manage.py test polls
```
This command:
- creates a special database for the purpose of testing. The contents of the database have the
  scope of a unit test, that is, the database is emptied as after each test finishes.
- finds a subclass of the django.test.TestCase class in file _test.py_
- looks for methods whose names begin with "test"

**Mocking a User:**  
A couple of features in Django allows me to mock a user in the interactive Django shell:
- `django.test.utils.setup_test_environment` installs a template renderer
- `django.test.Client` mimics a user entering URL's
Starting with the shell:
```shell
python manage.py shell
```
We enter the following statements:
```python
from django.test.utils import setup_test_environment
setup_test_environment()
from django.test import Client
client = Client()
from django.urls import reverse
response = client.get(reverse("polls:index"))  # HttpResponse for /polls/index.html  
```

**Some Best Testing Practices:**
- one `TestClass` for each `Model` or `View`
- one test method for each set of conditions you want to test

**In-Browser Testing Frameworks:**  
There are testing frameworks such as [Selenium](https://www.selenium.dev/) that
allows me to test _rendered_ HTML and the behavior of Web pages, namely JavaScript functionality.
For establishing that the correct template is being rendered and that the template
is passed the correct context data, I can use Django's test `client`.
