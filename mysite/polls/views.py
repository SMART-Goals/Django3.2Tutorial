# package imports
from polls.models import Choice, Question

# third party imports
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse
from django.utils import timezone

# standard imports
from typing import Union


class IndexView(generic.ListView):
    # These two lines substitute the old call to render(), which was
    # render(request, 'polls/index.html', {'latest_question_list': latest_question_list})
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self) -> QuerySet:
        """Return the last five published questions, from newest to oldest and
        not including those set to be publish in the future."""
        not_in_the_future = Question.objects.filter(pub_date__lte=timezone.now())  # a QuerySet
        return not_in_the_future.order_by("-pub_date")[:5]  # to be fed to `context_object_name`


class DetailView(generic.DetailView):
    r"""Assumed DetailView.as_view() will collect the Question.pk and the response template requires a
     context dictionary with only one key, key 'question' whose value is a Question object.
     """
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self) -> QuerySet:
        r"""Excludes any questions that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    r"""Assumed ResultsView.as_view() will collect the Question.pk and the response template requires a
     context dictionary with only one key whose value we chose to specifically store in
     `context_object_name`. The value associated to this key is a Question object.
     """
    model = Question
    template_name = 'polls/results.html'
    context_object_name = 'question'


def vote(request: HttpRequest, question_id: int) -> Union[HttpResponse, HttpResponseRedirect]:
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # reverse() is very similar to template tag {% url %}, it receives the namespaced address
        # instead of having to hardcode it
        url = reverse('polls:results', args=(question.id,))
        return HttpResponseRedirect(url)
