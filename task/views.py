# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Subject
from .serializers import SubjectSerializer
from rest_framework import status
# Create your views here.

def index(request):
    return render(request,'task/home.html',{})


class Home(APIView):
    def get(self,requst):
        subjects = Subject.objects.all()
        ser_data = SubjectSerializer(instance=subjects, many=True)
        return Response(ser_data.data , status= status.HTTP_200_OK)

    def post(self,request):
        srz_data = SubjectSerializer(data=request.data )
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status= status.HTTP_400_BAD_REQUEST)