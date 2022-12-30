from django.urls import path, include
from Poll.views import *

urlpatterns = [
    path('polllist/', PollList.as_view(), name='polllist'),
    path('questionlist/', QuestionList.as_view(), name='questionlist'),
    path('createpoll/', PollCreate.as_view(), name='createpoll'),
    path('createquestion/', QuestionCreate.as_view(), name='createquestion'),
    path('polllist/updatepoll/<pk>', PollUpdate.as_view(), name='updatepoll'),
    path('questionlist/updatequestion/<pk>', QuestionUpdate.as_view(), name='updatequestion'),
    path('polllist/deletepoll/<pk>', PollDelete.as_view(), name='deletepoll'),
    path('questionlist/deletequestion/<pk>', QuestionDelete.as_view(), name='deletequestion'),
]    