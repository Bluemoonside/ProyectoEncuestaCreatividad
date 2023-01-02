from django.urls import path, include
from Poll.views import *

urlpatterns = [
    path('list/', PollList.as_view(), name='polllist'),
    path('question/list/', QuestionList.as_view(), name='questionlist'),
    path('create/poll/', PollCreate.as_view(), name='createpoll'),
    path('create/question/', QuestionCreate.as_view(), name='createquestion'),
    path('list/update/poll/<pk>', PollUpdate.as_view(), name='updatepoll'),
    path('list/delete/poll/<pk>', PollDelete.as_view(), name='deletepoll'),
    path('question/list/update/question/<pk>', QuestionUpdate.as_view(), name='updatequestion'),
    path('question/list/delete/question/<pk>', QuestionDelete.as_view(), name='deletequestion'),
]    