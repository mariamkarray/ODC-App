from multiprocessing import AuthenticationError
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import StudentSerializer, UserSerializer
from rest_framework.response import Response
from .models import User, Student, StudentProgress
from courses.models import Course, Skill
from django.http import JsonResponse
import jwt, datetime
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from students import serializers

# Student list
@api_view(['GET'])
def student_list(request, format=None):
    # get users, serialize them, return json
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    # return a dictionary in order to be serialized
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def student_detail(request, id, format=None):
    try:
        student = Student.objects.get(pk=id)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def user_list(request, format=None):
    # get users, serialize them, return json
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    # return a dictionary in order to be serialized
    return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def user_detail(request, id, format=None):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

class register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found.')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password.')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8') 

        return Response({
            "jwt": token
        })

