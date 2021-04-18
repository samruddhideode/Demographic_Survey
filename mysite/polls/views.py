from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
# Create your views here.

from polls.models import Question


def index(request):
    question_list = Question.objects.all()
    context = {'question_list': question_list}
    return render(request, 'polls/index.html', context)


def details(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'polls/details.html', context)


def results(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = Question.objects.get(id=question_id)
    selected_choice = question.choice_set.get(id=request.POST['choice'])
    selected_choice.no_votes += 1
    selected_choice.save()

    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def view_all_results(request):
    all_ques = Question.objects.all()
    context = {'all_ques': all_ques}
    return render(request, 'polls/view_all_results.html', context)
