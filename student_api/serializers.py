from rest_framework import serializers
from .models import Subject
from django.contrib.auth.models import User


class SubjectSerializer(serializers.ModelSerializer):
    teacher = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='username')
    class Meta:
        model = Subject
        fields = ['id','subject_name','subject_class','teacher']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']
