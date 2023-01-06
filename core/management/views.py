from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response
from .models import UserModel,Doctor,Reports,Courses,Docterpatient,Tests
from .serializers import UserInfoserializer,DocterInfoserializer,ReportsInfoserializer,CoursesInfoserializer,DocterpatientInfoserializer,TestspatientInfoserializer
from rest_framework import status 


# create the user
@api_view(['POST'])
def CreateUser(request):
    print(request.data)
    try:
        serializer=UserInfoserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("data saved")

    except serializers.ValidationError as e:
        return Response({"error":e.detail},status=status.HTTP_400_BAD_REQUEST)


# create the docter
@api_view(['POST'])
def CreateDocter(request):
    print(request.data)
    try:
        serializer=DocterInfoserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("data saved")

    except serializers.ValidationError as e:
        return Response({"error":e.detail},status=status.HTTP_400_BAD_REQUEST)











@api_view(['GET'])
def Userdata(request):
    data=UserModel.objects.all()
    data=UserInfoserializer(data,many=True)
    return Response(data.data)


@api_view(['GET'])
def Doctersdata(request):
    data=Doctor.objects.all()
    data=DocterInfoserializer(data,many=True)
    return Response(data.data)

@api_view(['GET'])
def Reports_user(request,pk):
    data=Reports.objects.filter(user=pk)
    print(data)
    data=ReportsInfoserializer(data,many=True)
    return Response(data.data)

@api_view(['GET'])
def Courses_users(request,pk):
    data=Courses.objects.filter(user=pk)
    print(data)
    data=CoursesInfoserializer(data,many=True)
    return Response(data.data)


@api_view(['GET'])
def Docter_patients(request,pk):
    data=Docterpatient.objects.filter(doctor=pk)
    print(data)
    data=DocterpatientInfoserializer(data,many=True)
    return Response(data.data)



@api_view(['GET'])
def Tests_data(request,pk):
    data=Tests.objects.filter(user=pk)
    print(data)
    data=TestspatientInfoserializer(data,many=True)
    return Response(data.data)





#login the user
@api_view(['POST'])
def UserRegister(request):
    email=request.data['email']
    password=request.data['password']
