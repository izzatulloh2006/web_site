from cProfile import Profile
from http.client import responses
from tokenize import Token

from drf_yasg.openapi import Response, Contact
from rest_framework.viewsets import ModelViewSet
from apps.models import Category, Product, User
from apps.serializer import CategorySerializer, ProductSerializer, RegisterModelSerializer, ReactSerializer, \
    ServiceSerializer, ContactSerializer, LoginSerializer, ProfilUserModelSerializer
from .models import React , Service, Contacts
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework import generics
from apps.email_send import send_email
from apps.utils import send_custom_email
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# class SendEmailAPIView(APIView):
#     def post(self, request):
#         subject = request.data.get('subject')
#         message = request.data.get('message')
#         recipient_list = request.data.get('recipient_list')
#
#         if not subject or not message or not recipient_list:
#             return Response({"error": "Barcha maydonlarni to'ldiring."}, status=status.HTTP_400_BAD_REQUEST)
#
#         try:
#             send_custom_email(subject, message, recipient_list)
#             return Response({"success": "Xabar muvaffaqiyatli yuborildi!"}, status=status.HTTP_200_OK)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        response = super().post(request, *args, **kwargs)
        if serializer.is_valid():
            user = serializer.data.serializer.user
            response.data['user'] = {
                'user_id' : user.id,
                'first_name' : user.first_name,
                'last_name' : user.last_name,
                'email' : user.email,
            }
            return response


class LoginTokenView(TokenObtainPairView):
    def post(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        response = super().post(request, *args, **kwargs)
        if serializer.is_valid():
            user = serializer.data.serializer.user
            response.data['user'] = {
                'first_name': user.first_name,
                'last_name': user.last_name,
                'phone_number' : user.phone_number,
            }
        return response


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer
    pagination_class = None


class LoginViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    @api_view(['POST'])
    def login_view(self, request):
        phone_number = request.data.get('phone_number')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(username=phone_number, password=password)

        if user is not None:
            # Login successful
            return JsonResponse({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            # Login failed
            return JsonResponse({'error': 'Invalid phone number or password'}, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         response = super().post(request, *args, **kwargs)
#         if serializer.is_valid():
#             user = serializer.validated_data['user']
#
#
#         return response



# class SendEmailAPI(APIView):
#     def post(self, request):
#         subject = request.data.get('subject')
#         message = request.data.get('message')
#         to_email = request.data.get('to_email')
#
#         if not subject or not message or not to_email:
#             return Response({"error": "Barcha maydonlar to'ldirilishi shart."}, status=status.HTTP_400_BAD_REQUEST)
#
#         result = send_email(subject, message, to_email)
#
#         if result == "Xabar muvaffaqiyatli yuborildi!":
#             return Response({"success": result}, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": result}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ContactCreate(generics.CreateAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactSerializer


class ServiceListCreate(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer



class UserCreateAPIView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer

    def get(self, request):
        users = User.objects.all()
        serializer = RegisterModelSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RegisterModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreateAPIViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer
    pagination_class = None

    # def get(self, request):
    #     output = [{'phone_number': output.phone_number,
    #                'username': output.username}
    #               for output in User.objects.all()]
    #     return Response(output)
    #


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ReactViewSet(ModelViewSet):
    queryset = React.objects.all()
    serializer_class = ReactSerializer

    def get(self, request):
        output = [{'firstname': output.firstname,
                   'lastname': output.lastname,
                   'age': output.age}
                  for output in React.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


class ProfilViewSet(ModelViewSet):
    queryset = Profile
    serializer_class = ProfilUserModelSerializer
