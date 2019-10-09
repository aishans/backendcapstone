from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# Create your views here.


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]


class SchoolListView(ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolListSerialzer
    # filter_backends = [OrderingFilter, ]


class CategoryListView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerialzer
    lookup_field = 'id'
    lookup_url_kwarg = 'category_id'


class SubjectDetailListView(RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectDetailListSerialzer
    lookup_field = 'id'
    lookup_url_kwarg = 'subject_id'


class SubjectQuestionListView(RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectQuestionListSerialzer
    lookup_url_kwarg = 'questions_id'
