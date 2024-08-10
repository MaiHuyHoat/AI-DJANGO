from django.urls import path
from . import views
from . import api
urlpatterns = [
     path('',views.index,name='QA.index'),
     path('api/v1/QA',api.getQA,name='QA.api'),
     path('api/v1/summarization',api.getSummarization,name='QA.api.summarazation')
]
