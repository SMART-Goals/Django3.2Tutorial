**Dealing with POST data:**  
The `form` header contains the URL, hence the view function, in charge of processing the form.
In the case below, `/polls/{{question_id}}/vote` or function `polls.views.vote`
```html
<form action="{% url 'polls:vote' question.id %}" method="post">
```

The values `polls.view.vote` will receive are specified in the form within `<input>` tags. These are
collected in dictionary `request.POST`. Recall `request` is the first mandatory argument for all views.

In this part4, file `polls/detail.html` contains two `<input>` tags:
```html
<input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
<input type="submit" value="Vote">
```
which will be gathered into `request.POST = {"choice": choice.id, "submit": "Vote"}`

View `polls.views.vote` returns and `HttpResponseRedirect` object instead of an `HttpResponse` object.
`HttpResponseRedirect` will void `request.POST` so that if user hits the Back button,
`{% url 'polls:vote' question.id %}` won't cause the vote tally of the previously selected choice to
increase again.

**Generic Views:**  
Generic views abstract common patterns such as getting data from the database according to
a parameter passed in the URL, loading a template and returning the rendered template.
