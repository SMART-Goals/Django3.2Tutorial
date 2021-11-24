# third party packages
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

    def was_published_recently(self) -> datetime.datetime:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


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
