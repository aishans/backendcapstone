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
        model = Profile
        fields = "__all__"


class SubjectListSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subject_name']


class CategoryListSerialzer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ["category", "subjects"]

    def get_subjects(self, obj):
        subject = Subject.objects.filter(category_subject=obj)
        return SubjectListSerialzer(subject, many=True).data


class SchoolListSerialzer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ["school_name", "categories"]

    def get_categories(self, obj):
        category = Category.objects.filter(classification=obj)
        return CategoryListSerialzer(category, many=True).data


class SubjectDetailListSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class AnswerListSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ["is_correct", "answer"]


class QuestionAnswerListSerialzer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ["questions", "answers"]

    def get_answers(self, obj):
        rightanswer = Answer.objects.filter(question=obj)
        return AnswerListSerialzer(rightanswer, many=True).data


class SubjectQuestionListSerialzer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Subject
        fields = ["subject_name", "questions"]

    def get_questions(self, obj):
        subquestions = Question.objects.filter(subject=obj)
        return QuestionAnswerListSerialzer(subquestions, many=True).data
