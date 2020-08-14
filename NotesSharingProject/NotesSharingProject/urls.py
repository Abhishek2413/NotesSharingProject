"""NotesSharingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from notes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('',views.index,name='index'),
    path('login',views.userlogin,name='login'),
    path('login_admin',views.login_admin,name='login_admin'),
    path('signup',views.signup1,name='signup'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('logout',views.Logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('view_user',views.View_User,name='view_user'),
    path('delete_user/<int:pid>',views.Delete_User,name='delete_user'),
     

]
