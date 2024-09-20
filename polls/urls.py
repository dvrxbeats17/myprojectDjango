from xml.etree.ElementInclude import include
from django.urls import path, re_path,reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView

from . import views

app_name = "polls"
urlpatterns = [
    re_path(r"^index/$", views.index, name="index"),
    path("<int:question_id>/", views.QuestionRedirectView.as_view(), name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path("all", views.all, name="all"),
    path("first/<int:question_number>/", views.number, name="firsr-N"),
    path("create/", views.create, name="create"),
    path("delete/", views.delete, name="delete"),
    path("change/", views.change, name="change"),
    path("choice-question/", views.choice_to_question, name="choice-to-question"),
    path("question-choice/", views.question_to_choice, name="question-to-choice"),
    path('latest/', views.latest, name='latest'),
    path('count/', views.count, name='count'),
    path('agregate/', views.agregate, name='agregate'),
    path('annotate/', views.annotate, name='anotate'),
    path('avg/', views.avg, name='avg'),
    path('concat/', views.concat, name='concat'),
    path('all_questions', views.all_questions, name='all_questions'),
    path('delete_id/<int:question_number>',views.delete_id, name='delete-by-id'),
    path('find/<str:question_str>/', views.get_question,name='find-question'),
    path('get_id/<int:question_id>', views.get_id, name="get_by_id"),
    path('hello', views.HelloWorld.as_view(), name="hello-world"),
    path('detail-first', views.QuestionDetailView.as_view(), name='detail-first'),
    path('detail/<int:pk>', views.QuestionDetail.as_view(), name='question-detail'),
    path('list', views.QuestionList.as_view(), name='list-question'),
    path('choice-list/<int:vote>', views.ChoiceListView.as_view(), name='choice-list'),
    path('q_formview', views.QuestionFormView.as_view(), name='q-formV'),
    path('q_createview', views.QuestionCreateView.as_view(), name='q-createV'),
    path('q_updateview/<int:pk>/', views.QuestionUpdateView.as_view(),name='q-updateV'),
    path('q_deletev/<int:pk>/', views.QuestionDeleteView.as_view(), name='q-deleteV'),
    path('q_paginator', views.paginator, name='q-paginator'),
    path('login', LoginView.as_view(template_name="polls/login.html",next_page='polls:index'), name='login'),
    path('logout', LogoutView.as_view(next_page='polls:index'), name='logout'),
    path('pass-reset', PasswordResetView.as_view(template_name='polls/password-reset.html', success_url=reverse_lazy('password-reset-done')),name='password-reset'),
    path('pass-reset-done',PasswordResetDoneView.as_view(template_name='polls/password-done.html'),name='password-reset-done'),
    path('password_reset_confirm/<str:uidb64>/<str:token>}',  PasswordResetConfirmView.as_view(template_name='registration/password_reset_email.html'), name='password_reset_confirm'),
    path('custom-f', views.custom_filter, name='custom-filter'),
]
