from django.urls import path, include
from .Views.PollViews import PollListView, PollCreateView, PollUpdateView, PollDeleteView
from .Views.QuestionViews import QuestionListView, QuestionCreateView, QuestionUpdateView, QuestionDeleteView
from django.conf.urls import handler404, handler500, handler403
from AccesControl.views import Error403, Error404, Error500

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

handler404 = Error404.as_view()
handler403 = Error403.as_view()
handler500 = Error500.as_error_view()