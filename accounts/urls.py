from multiprocessing import AuthenticationError
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.LoginPageView.as_view(), name='login'),
    path('logout/', views.LoggingOutView.as_view(), name='logout'),
    path('', views.DashboardView.as_view(), name='dashboard'),
]