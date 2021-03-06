from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views


router = DefaultRouter()
router.register(r'check-list', views.CheckListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('login', views.login_user)
]
