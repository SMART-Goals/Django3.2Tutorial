# third party imports
from django.contrib import admin

# package imports
from polls.models import Choice, Question


admin.site.register(Choice)
admin.site.register(Question)
