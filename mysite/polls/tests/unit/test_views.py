# package imports
from polls.models import Question

# third party imports
from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

# standard imports
import datetime


def create_question(question_text, days):
    r"""(helper function)
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    # Question.objects.create() instantiates a Question and saves it to the (testing) database
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        # self.client mimics a user, self.client.get() mimics the user entering a URL in the browser
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )


class QuestionDetailViewTests(TestCase):

    def get_response(self, future_question=False, question_text="A Question") -> HttpResponse:
        r"""Helper function to instantiate a Question in the past or in the future"""
        days_in_the_future = 1 if future_question else -1
        a_question = create_question(question_text=question_text, days=days_in_the_future)
        url = reverse('polls:detail', args=(a_question.pk,))
        return self.client.get(url)

    def test_future_question(self):
        r"""The detail view of a question with a pub_date in the future returns a 404 not found."""
        response = self.get_response(future_question=True)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        r"""The detail view of a question with a pub_date in the past displays the question's text."""
        question_text = "Not another question!"
        response = self.get_response(question_text=question_text, future_question=False)
        self.assertContains(response, question_text)
