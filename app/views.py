from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter,OrderingFilter
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# Create your views here.
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

class SchoolsListView(ListAPIView):
    queryset = Schools.objects.all()
    serializer_class = SchoolListSerialzer
    filter_backends = [ OrderingFilter,]
    permission_classes = [IsAuthenticated]

class CategoryElementaryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryElementaryListSerialzer
    permission_classes = [IsAuthenticated]

class CategoryMiddleSchoolListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryElementaryListSerialzer
    permission_classes = [IsAuthenticated]

class CategoryHighSchoolListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryHighSchoolListSerialzer
    permission_classes = [IsAuthenticated]

