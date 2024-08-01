from django.contrib.auth.hashers import make_password
from rest_framework.fields import CharField
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from apps.models import Category, Product, User, React
from rest_framework.permissions import IsAuthenticated


class RegisterModelSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = 'phone_number', 'password', 'confirm_password', 'first_name', 'last_name'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        confirm_password = data.pop('confirm_password')
        if confirm_password and confirm_password == data['password']:
            data['password'] = make_password(data['password'])
            return data
        raise ValidationError("Passwords don't match")

    def validate_phone_number(self, phone_number):
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("Bu raqam allaqachon ro'xatda mavjud!")
        return phone_number


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'balance', 'bot_options',
                   'has_registered_bot', 'not_read_message_count', 'is_active',
                   'is_superuser', 'is_staff', 'payme_balance', 'last_login', 'phone_number', 'email',
                   "tg_id", "type", 'date_joined', 'password'
                   )

        def validate_password(self, password):
            return make_password(password)


class UpdateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'photo'
        permission_classes = (IsAuthenticated,)


class UpdatePasswordUserSerializer(ModelSerializer):
    confirm_password = CharField(max_length=255)

    class Meta:
        model = User
        fields = 'password', 'confirm_password'
        # extra_kwargs = {
        #     'password': {'write_only': True}
        # }
        permission_classes = (IsAuthenticated,)

    def validate(self, data):
        confirm_password = data.pop('confirm_password')
        if confirm_password and confirm_password == data['password']:
            data['password'] = make_password(data['password'])
            return data
        raise ValidationError("Password error")


class UserDetailModelSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ('groups', 'user_permissions', 'password')


# class RegisterModelSerializer(ModelSerializer):
#     confirm_password = CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = 'phone_number', 'password', 'confirm_password', 'first_name', 'last_name'
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }
#
#     def validate(self, data):
#         confirm_password = data.pop('confirm_password')
#         if confirm_password and confirm_password == data['password']:
#             data['password'] = make_password(data['password'])
#             return data
#         raise ValidationError("Passwords don't match")
#
#     def validate_phone_number(self, phone_number):
#         if User.objects.filter(phone_number=phone_number).exists():
#             raise ValidationError("Bu raqam allaqachon ro'xatda mavjud!")
#         return phone_number


class ReactSerializer(ModelSerializer):
    class Meta:
        model = React
        fields = ['firstname', 'lastname', 'age']
