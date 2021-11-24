**Template resolution:**  
By convention DjangoTemplates looks for a `templates/` subdirectory _in each of_ the INSTALLED_APPS. Thus, if
we have `polls/templates/index.html`, directory `polls/templates` will be registered as one of the
template directories. We can pass the template name `index.html` to a view and it will find file
`polls/templates/index.html`, unless there's another `index.html` in one of the other template directories.
To avoid this potentially unintended behaviour, we can create file `polls/templates/polls/index.html` and
pass the template name `polls/index.html` in the view. It just requires creation of one `polls/` subdirectory.
In Django parlance, we have _namespaced_ template `index.html`.

**Referecing Internal Pages:**  
If we're including a hyperlink to an internal page, don't hardcode the address but instead use the
_namespacing_ features of the URLConf files. For instance, file `polls/urls.py`:
```python
app_name = 'polls'
urlpatterns = [
    path('detailed/<int:question_id>/', views.detail, name='detail'),
]
```
Now within a template we can substitute `/polls/detailed/{{ question.id }}/` with the `url` tag
`{% url 'polls:detail' question.id %}`