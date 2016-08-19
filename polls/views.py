from django.http import HttpResponse
from django.template import RequestContext, loader

from django.shortcuts import get_object_or_404 , render
from .models import Question, Choice


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]

	template = loader.get_template('polls/index.html')
	context  = RequestContext(request,{'latest_question_list' : latest_question_list,})
	#the context is a dictionary mapping template variable names to python objects
	return HttpResponse(template.render(context))

#These polls have an argument, something different and new

def choiceindex(request):
	trending_choice_list = Choice.objects.order_by('votes')[:5]

	template = loader.get_template('polls/index.html')
	context  = RequestContext(request,{'trending_choice_list' : trending_choice_list,})
	#the context is a dictionary mapping template variable names to python objects
	return HttpResponse(template.render(context))

def detail(request , question_id):
	question  = get_object_or_404(Question, pk = question_id)
	return render(request , 'polls/details.html', {'question': question} )
	#return HttpResponse("You're looking at question %s." % question_id)

def results(request , question_id):
	response = "You are looking ath the results of the question %s ."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You are voting on the question %s . " % question_id)


