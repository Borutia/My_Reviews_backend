from django.contrib.auth import user_logged_in
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import exceptions

from accounts.models import User
from accounts.serializers import Registration_serializer, Login_serializer


class Registration_API_View(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = Registration_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        check_save = serializer.save()
        if check_save:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response('Registration fail')

class Login_API_View(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            serializer = Login_serializer(data=request.data)
            serializer.is_valid(raise_exception=False)
            user = User.objects.get(email=serializer.data['email'],
                                    password=serializer.data['password'])
            user_logged_in.send(sender=user.__class__,
                                request=request, user=user)
            token, created = Token.objects.get_or_create(user=user)
            response = Response(serializer.data['email'], status=status.HTTP_200_OK)
            response.set_cookie('My_Reviews', token.key)
            return response
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('Incorrect email or password')


