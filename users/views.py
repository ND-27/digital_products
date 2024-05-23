from django.shortcuts import render

<<<<<<< HEAD
# Create your views here.
=======
from django.core.cache import cache

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, Device, UserToken


class RegisterView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')
        refresh_token = request.data.get('refresh_token')

        print(refresh_token)

        if not phone_number:
            return Response({'message': 'phone number required'}, status=status.HTTP_400_BAD_REQUEST)

        if refresh_token:
            return Response({'message': 'User already registered'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(phone_number=phone_number)

        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number)

        # # its not good because create new user without username.
        # user, created = User.objects.get_or_create(phone_number=phone_number)
        #
        # if not created:
        #     return Response({'message': 'User already registered'}, status=status.HTTP_400_BAD_REQUEST)

        code = random.randint(100000, 999999)

        # send_message (sms or email)

        # cache
        cache.set(str(phone_number), code, 2 * 60)

        return Response({'message': 'Your verification code', 'code': code}, status=status.HTTP_201_CREATED)


class GetTokenView(APIView):

    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        cached_code = cache.get(str(phone_number))

        if code != cached_code:
            return Response({'message': 'Invalid code'}, status=status.HTTP_403_FORBIDDEN)

        user = User.objects.get(phone_number=phone_number)
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)
        refresh_token = str(refresh)

        device, created = Device.objects.get_or_create(user=user)

        UserToken.objects.create(user=user, device=device, token=refresh_token)

        return Response({'access': access, 'refresh': refresh_token}, status=status.HTTP_200_OK)


class LogoutView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        try:
            user_token = UserToken.objects.get(token=refresh_token)
        except UserToken.DoesNotExist:
            return Response({'message': 'Token not found'}, status=status.HTTP_404_NOT_FOUND)

        user_token.delete()
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
>>>>>>> eb7f400 (Complete 'users' app and add Logout view and get and use JWT in viwes.urls.py and use it in Logout and viewing product list.)
