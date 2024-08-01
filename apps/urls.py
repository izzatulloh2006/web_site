from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.views import CategoryViewSet, ProductViewSet, UserCreateAPIViewSet, ReactViewSet, UserCreateAPIView


router = DefaultRouter()
router.register(r'categories', CategoryViewSet, 'category')
router.register(r'product', ProductViewSet, 'product')
router.register(r'users', UserCreateAPIViewSet, 'users')
router.register(r'start', ReactViewSet,  'start')


urlpatterns = [
    path('', include(router.urls)),
    path('user/register/', UserCreateAPIView.as_view(), name='token_obtain_pair'),

]
