"""crud_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud import views
from crud.views import CustomAuthToken,RegisterAPI
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('auth/login/',jwt_views.TokenObtainPairView.as_view(), name='login_api'),
    # path('example/',views.example_view,name='profile_API'),
    path('profile/',views.ProfileView.as_view(),name='profile_API'),
    path('admin/', admin.site.urls),
    path('all/', views.All_Users,name="all_user"),
    path('reg/', views.Register_Api_View,name="reg"),
    path('home/', views.All_Products,name="home"),
    path('del/<str:pk>/', views.Del_Product,name="del"),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
