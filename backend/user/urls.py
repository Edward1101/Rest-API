from . import views
from django.urls import path

urlpatterns = [
    path('', views.UsersAPIView.as_view()),
    path('<int:pk>/', views.UserAPIView.as_view(), name='user-detail'),

]
