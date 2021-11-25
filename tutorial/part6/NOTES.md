**Static Files:**  
Additional files such as images, JavaScript, or CSS that need to be incorporated in the final rendered
HTML pages.

`django.contrib.staticfiles` is a default plugged-in App that collects static files from each App in the
project into a single location that can be served.
By default, Django will look under `App/static/` directories (e.g `polls/static/`) but additional
directories can be specified.

**Namespacing Static Files:**  
Similarly to namespacing templates, by creating file `polls/static/polls/style.css` I'll be able to
reference this file just as `polls/style.css` since `polls/static/` is collected by
`django.contrib/staticfiles`. Subdirectory `polls/` in `polls/style.css` removes any ambiguity in the
scenario where more than one App contains a `style.css` file.

**Restarting the Development Server:**  
If developing, you need to restart the server in order for the newly added static files
to show up when rendering the HTML pages.

**Adding Images:**  
Adding an image to the `polls` App and referring it in CSS file _polls/static/polls/style.css_:
```ccs
body {
    background: white url("images/background.gif") no-repeat;
}
```
This file is `polls/static/polls/images/background.gif`. Thus, notice how we must pass the relative
path of the image with respect to `dirname(polls/static/polls/style.css)`. We cannot use
the `{% static %}` tag in static files because static files are not scanned by Django.