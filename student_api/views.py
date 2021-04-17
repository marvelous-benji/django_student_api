from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SubjectSerializer, UserSerializer
from .models import Subject
from django.contrib.auth.models import User

# Create your views here.

@api_view(['GET'])
def welcome_page(request):
    return Response({'msg':'Welcome to Student Api'},status=status.HTTP_200_OK)

@api_view(['GET'])
def get_subjects(request):
    try:
        subjects = Subject.objects.all()
        subject_serializer = SubjectSerializer(subjects,many=True)
        return Response({'status':'success','subjects':subject_serializer.data},status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({'status':'failed','msg':'an error occured'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_subject(request,pk):
    try:
        subject = Subject.objects.filter(pk=pk).first()
        if subject:
            subject_serializer = SubjectSerializer(subject)
            return Response({'status':'success','subject':subject_serializer.data},status=status.HTTP_200_OK)
        return Response({'status':'failed','msg':'resource not found'},status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response({'status':'failed','msg':'an error occured'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def add_subject(request):
    try:
        data = request.data
        ad = User.objects.get(pk=1)
        mydata = {'subject_name':data['subject_name'],'subject_class':data['subject_class'],'teacher':ad}
        serialize_subject = SubjectSerializer(data=mydata)
        if serialize_subject.is_valid():
            print('i ran')
            serialize_subject.save()
            return Response({'status':'success','msg':'subject added successfully'},status=status.HTTP_201_CREATED)
        return Response({'status':'failed','msg':'input is invalid'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    except Exception as e:
        print(e)
        return Response({'status':'failed','msg':'some required data fields are missing'},status=status.HTTP_406_NOT_ACCEPTABLE)



@api_view(['PUT'])
def update_subject(request,pk):
    try:
        data = request.data
        subject = Subject.objects.filter(pk=pk).first()
        if subject:
            subject.subject_name = data.get('subject_name',subject.subject_name)
            subject.subject_class = data.get('subject_class',subject.subject_class)
            subject.teacher_id = data.get('teacher_id',subject.teacher_id)
            subject.save()
            print(subject)
            subject_serializer = SubjectSerializer(subject)
            return Response({'status':'success','subject':subject_serializer.data},status=status.HTTP_200_OK)
        return Response({'status':'failed','msg':'Subject not found'},status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response({'status':'failed','msg':'Invalid input'},status=status.HTTP_422_UNPROCESSABLE_ENTITY)



@api_view(['DELETE'])
def delete_subject(request,pk):
    try:
        subject = Subject.objects.filter(pk=pk).first()
        if subject:
            subject.delete()
            return Response({'status':'success','msg':'subject deleted successfully'},status=status.HTTP_204_NO_CONTENT)
        return Response({'status':'failed','msg':'subject not found'},status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(e)
        return Response({'status':'failed','msg':'An error occured'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
