from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Choice, Question

def index(request):
   questoes = Question.objects.all()

   questoes_str = "<br>".join([str(questao.question_text) for questao in questoes])

   return HttpResponse("Hello, world. You're at the polls index.<br>" + questoes_str)
