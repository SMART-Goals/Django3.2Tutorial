r"""
polls.views module before the introduction of generic views
"""

# package imports
from polls.models import Choice, Question

# third party imports
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# standard imports
from typing import Union


def index(request: HttpRequest) -> HttpResponse:
    # fetch last five questions, from newest to oldest
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    # notice question is not a string but a Question object. Function render() will call Question.__str__()
    # and pass the result to template polls/detail.html
    return render(request, 'polls/detail.html', {'question': question})


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


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
