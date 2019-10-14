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
                       CategoryListView, SubjectDetailListView, SubjectQuestionListView, SubjectListView, ProfileAPIView, ProfileUpdateAPIView,)
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('signup/', UserCreateAPIView.as_view(), name='signup'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateAPIView.as_view(), name='profile-update'),
    path('schoollist/', SchoolListView.as_view(), name='api-schools'),
    path('subjectlist/<int:category_id>/',
         SubjectListView.as_view(), name='api-schools'),
    path('categorylist/<int:school_id>/',
         CategoryListView.as_view(), name='api-category'),
    path('subjectdetail/<int:subject_id>/',
         SubjectDetailListView.as_view(), name='api-subjectDetail'),
    path('questionlist/<int:subject_id>/',
         SubjectQuestionListView.as_view(), name='api-subject-questions'),




]
