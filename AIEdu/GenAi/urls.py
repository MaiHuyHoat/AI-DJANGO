"""
URL configuration for AIEdu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from . import api
urlpatterns = [
     path('GenCode',views.genCode,name='GenAi.GenCode'),
     path('GenTranlate',views.genTranslate,name='GenAi.GenTranslate'),
     path('SummaryParagraph',views.summaryParagraph,name='GenAi.SummaryParagraph'),
     path('GenQuestion',views.genQuestion,name='GenAi.GenQuestion'),
     path('api/v1/gpt4all',api.getAnswer,name='GenAi.api.getAnswer'),
     path('api/v1/textToSpeed',api.textToSpeech,name='GenAi.api.textToSpeed'),
]
