from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('food/',include('FoodApp.urls')),
    path('users/',include('users.urls')),
    path('',views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),

]