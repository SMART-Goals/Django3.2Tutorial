# third party imports
from django.contrib import admin

# package imports
from polls.models import Choice, Question


class QuestionAdmin(admin.ModelAdmin):
    # Summary of relevant features of each question when all questions are presented
    # notice we can include Question class attributes as well as bounded methods that take no arguments
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # adds a “Filter” sidebar with default options for filtering by date
    list_filter = ['pub_date']

    # Include at the top of the page a search field will be restricted to searching the Questions' text.
    search_fields = ['question_text']

    # Customize how each Question will be presented in its dedicated page
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

    # Show assoicated choices for each Question when presented in its dedicated page
    class ChoiceInline(admin.TabularInline):
        r"""Present the choices associated with the Question, plus one blank Choice that can be filled"""
        model = Choice
        extra = 1
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
