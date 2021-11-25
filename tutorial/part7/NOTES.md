**Customizing the Admin Form:**
Notes have been added as code comments in `polls/admin.py` and `polls/models.py`.

The admin site is a site of the project, even though the only devoted module I wrote is `polls/admin.py`.
This module is actually the _contribution_ of App `polls` to the project's admin site.

**Templates for the Admin site:**  
Since the admin site belong to the projct, the `templates/` directory should reside under the top
`mysite/` directory. We signal this to `mysite/settings.TEMPLATES`
```python
'DIRS': [BASE_DIR / 'templates']
```
Any of Django’s default admin templates can be overridden. To override a template, copy it from the
default directory into your custom directory, and make changes. That's what I did with
`templates/admin/base_html`, taken from 
`$PYTHON_CONDA_ENV/lib/python3.8/site-packages/django/contrib/admin/templates/admin/base_site.html`.
