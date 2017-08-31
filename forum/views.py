from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Question


# Create your views here.

def index(request):
    questions = Question.objects.all().order_by("-id")[:10]
    return render(request, 'forum/index.html', {"questions": questions})
