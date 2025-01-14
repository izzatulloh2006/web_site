from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.views import (CategoryViewSet, ProductViewSet, UserCreateAPIViewSet, ReactViewSet,
                        UserCreateAPIView, ServiceListCreate, ServiceDetail, ContactCreate,
                        LoginTokenView, LoginViewSet, TokenObtainPairView, CustomTokenObtainPairView)
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, 'category')
router.register(r'product', ProductViewSet, 'product')
router.register(r'users', UserCreateAPIViewSet, 'users')
router.register(r'start', ReactViewSet,  'start')
# router.register(r'register', UserCreateAPIView, 'register')
router.register(r'login', LoginViewSet, 'login')
router.register(r'profile', ProductViewSet,  'profile')


urlpatterns = [
    path('', include(router.urls)),
    path('token/', LoginTokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('user/register/', UserCreateAPIView.as_view(), name='token_obtain_pair'),

    # path('login1', LoginViewSet, name='login1'),
    # path('register/', UserCreateAPIView.as_view(), name='user-register'),
    # path('user/register/', UserCreateAPIView.as_view(), name='token_obtain_pair'),
    # path('services/', ServiceListCreate.as_view(), name='service-list-create'),
    # path('services/<int:pk>/', ServiceDetail.as_view(), name='service-detail'),
    # path('contact/', ContactCreate.as_view(), name='contact-create'),
    # path('send-email/', SendEmailAPI.as_view(), name='send-email'),
    # path('send-email/', SendEmailAPIView.as_view(), name='send-email'),
    # path('login/', LoginView.as_view(), name='login'),
]
