
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse

# Create your views here.
def index(request):
    template = loader.get_template('QA/index.html')
    context={
        'urlGenAiApi': reverse("GenAi.api.getAnswer"),
        'urlQA': reverse("QA.api"),
        'urlTextToSpeech':reverse("GenAi.api.textToSpeed"),
         'urlSummarazationVietAi': reverse("QA.api.summarazation")
    }
    return HttpResponse(template.render(context,request))
