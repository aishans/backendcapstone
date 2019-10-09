"""backendd URL Configuration

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
from app.views import (UserCreateAPIView, SchoolListView,
                       CategoryListView, SubjectDetailListView, SubjectQuestionListView, )
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('schools/', SchoolListView.as_view(), name='api-schools'),
    path('schools/<int:category_id>/',
         CategoryListView.as_view(), name='api-category'),
    path('subject/<int:subject_id>/',
         SubjectDetailListView.as_view(), name='api-subjectDetail'),
    path('questions/<int:questions_id>/',
         SubjectQuestionListView.as_view(), name='api-subject-questions'),




]
