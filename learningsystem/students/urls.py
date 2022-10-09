from django.contrib import admin
from django.urls import path, include
from .views import register, LoginView, user_list, student_detail, student_list
from students import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('register/', register.as_view()),
    path('login', LoginView.as_view()),
    path('users/', views.user_list),
    path('user/<int:id>', views.user_detail),
    path('student/<int:id>', views.student_detail),
    path('students/', views.student_list),
]
# getting json format response instead of the html view
urlpatterns = format_suffix_patterns(urlpatterns)