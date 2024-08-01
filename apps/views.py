from drf_yasg.openapi import Response
from rest_framework.viewsets import ModelViewSet
from apps.models import Category, Product, User
from apps.serializer import CategorySerializer, ProductSerializer, RegisterModelSerializer, ReactSerializer
from .models import React
from rest_framework.generics import CreateAPIView


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer
    # pagination_class = None

    def get(self, request):
        output = [{'phone_number': output.phone_number,
                   'password': output.password,
                   'confirm_passwor': output.confirm_passwor,
                   'first_name': output.first_name,
                   'last_name': output.last_name}
                  for output in React.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


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


