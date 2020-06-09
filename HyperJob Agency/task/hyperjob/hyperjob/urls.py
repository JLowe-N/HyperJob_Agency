"""hyperjob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from django.views import View
from .views import IndexView
from resume.views import ResumeBaseView
from vacancy.views import VacancyBaseView
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, login as auth_login
from django.views.generic import CreateView, RedirectView


class MyLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    authentication_form = AuthenticationForm

class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login'
    template_name = 'signup.html'


urlpatterns = [
    path('resumes', ResumeBaseView.as_view()),
    path('vacancies', VacancyBaseView.as_view()),
    path('admin', admin.site.urls),
    path('login', MyLoginView.as_view()),
    path('login/', RedirectView.as_view(url='login')),
    path('signup', MySignupView.as_view()),
    path('signup/', RedirectView.as_view(url='signup')),
    path('logout', LogoutView.as_view()),
    path('logout/', RedirectView.as_view(url='logout')),
    path('', IndexView.as_view()),

]

