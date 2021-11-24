# third party imports
from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

# package imports
from polls.models import Question


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
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}.")
