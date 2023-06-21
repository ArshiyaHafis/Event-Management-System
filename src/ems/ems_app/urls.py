from django.urls import path
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('regsiter/', views.register, name='register'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('event/', views.get_event, name='event'),
    path('add_event/', views.post_event, name='add_event'),
    path('details/<int:id>', views.details, name='details'),
]
