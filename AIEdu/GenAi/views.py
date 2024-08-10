
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

# Create your views here.
def genCode(request):
    template = loader.get_template('GenAi/GenCode.html')
    context={
        'urlGenAiApi': reverse("GenAi.api.getAnswer")
    }
    return HttpResponse(template.render(context,request))
# Create your views here.
def genTranslate(request):
    template = loader.get_template('GenAi/GenTranslate.html')
    context={
        'urlGenAiApi': reverse("GenAi.api.getAnswer")
    }
    return HttpResponse(template.render(context,request))
def genQuestion(request):
    template = loader.get_template('GenAi/GenQuestion.html')
    context={
        'urlGenAiApi': reverse("GenAi.api.getAnswer")
    }
    return HttpResponse(template.render(context,request))
def summaryParagraph(request):
    template = loader.get_template('GenAi/SummaryParagraph.html')
    context={
        'urlGenAiApi': reverse("GenAi.api.getAnswer")
    }
    return HttpResponse(template.render(context,request))
