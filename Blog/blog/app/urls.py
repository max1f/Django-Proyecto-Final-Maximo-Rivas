from django.contrib import admin
from django.urls import path,include
from app import views
from .views import inicio,posts,about,contact,publicar,login_request,register,feed,profile
from django.contrib.auth.views import LogoutView,LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('#!', views.inicio),
    path('post', views.posts),
    path('about', views.about),
    path('contact', views.contact),
    path('feed', views.feed),
    path('login', LoginView.as_view(template_name='sign.html'), name='login'),
    path('register', views.register, name= 'register'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name= 'Logout'),
    path('profile/', views.profile, name='profile'),
]   
