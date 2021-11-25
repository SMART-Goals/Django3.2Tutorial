# third party packages
from django.contrib import admin
from django.db import models
from django.utils import timezone

# standard imports
import datetime


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')  # optional human-readable name for the database column

    def __str__(self) -> str:
        r"""Important because they're used in the admin pages"""
        return self.question_text

    # The `admin.display` decorator endows with functionality the column assigned to display whether
    # the question was published recently when presenting this feature of Question in the /admin/polls site.
    # In particular, we set the title of the column to 'Published recently?' and when we click on the
    # column header, the column items will be ordered by their `pub_date` values. Also, the option
    # `boolean=True` will replace the return value of the function (`True` or `False`) with fancy "+"
    # and "x" icons.
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self) -> datetime.datetime:
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    r"""We cannot save in the database a Choice unrelated to a question
    Wrong:
        Choice(question=q, choice_text="I'm rogue", votes=0).save()
    Correct: associate the Choice to the first Question stored in the database, and save the choice
        q = Question.objects.get(pk=1)
        Choice(question=q, choice_text="I'm rogue", votes=0).save()
    Correct: associate the Choice to the first Question stored in the database, and save the choice
        q = Question.objects.get(pk=1)
        q.choice_set.create(choice_text="I'm rogue", votes=0)
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # a Choice is related to a Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choice_text
