from django.urls import path, include
from .Views.PollViews import PollListView, PollCreateView, PollUpdateView, PollDeleteView
from .Views.QuestionViews import QuestionListView, QuestionCreateView, QuestionUpdateView, QuestionDeleteView

urlpatterns = [
    path('list/', PollListView.PollList.as_view(), name='polllist'),
    path('question/list/', QuestionListView.QuestionList.as_view(), name='questionlist'),
    path('create/poll/', PollCreateView.PollCreate.as_view(), name='createpoll'),
    path('create/question/', QuestionCreateView.QuestionCreate.as_view(), name='createquestion'),
    path('list/update/poll/<pk>', PollUpdateView.PollUpdate.as_view(), name='updatepoll'),
    path('question/list/update/question/<pk>', QuestionUpdateView.QuestionUpdate.as_view(), name='updatequestion'),
    path('list/delete/poll/<pk>', PollDeleteView.PollDelete.as_view(), name='deletepoll'),
    path('question/list/delete/question/<pk>', QuestionDeleteView.QuestionDelete.as_view(), name='deletequestion'),
]    