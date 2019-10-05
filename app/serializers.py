from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password", 'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data

class ProfileSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    class Meta:
        model= Profile
        fields= "__all__"

class SchoolListSerialzer(serializers.ModelSerializer):
    class Meta:
        model= School
        fields= "__all__"

class CategoryElementaryListSerialzer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= "__all__"

class CategoryMiddleSchoolListSerialzer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= "__all__"

class CategoryHighSchoolListSerialzer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= "__all__"




