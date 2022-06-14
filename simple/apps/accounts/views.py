#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
"""
Created on mon Jun  13 06:04:16 2022
@author: kmalesh
"""

from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import AllowAny

from simple.apps.accounts.serializers import UserRegistrationSerializer, UserLoginSerializer
from simple.apps.accounts.models import UserProfile


class UserRegistrationView(CreateAPIView):

    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            "success": "True",
            "status code": status_code,
            "message": "User registered  successfully",
        }

        return Response(response, status=status_code)


class UserLoginView(CreateAPIView):

    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            "success": "True",
            "status code": status.HTTP_200_OK,
            "message": "User logged in  successfully",
            "token": serializer.data["token"],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)


class UserProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                "success": "true",
                "status code": status_code,
                "message": "User profile fetched successfully",
                "data": [
                    {
                        "first_name": user_profile.first_name,
                        "last_name": user_profile.last_name,
                        "phone_number": user_profile.phone_number,
                        "age": user_profile.age,
                        "gender": user_profile.gender,
                    }
                ],
            }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                "success": "false",
                "status code": status.HTTP_400_BAD_REQUEST,
                "message": "User does not exists",
                "error": str(e),
            }
        return Response(response, status=status_code)
