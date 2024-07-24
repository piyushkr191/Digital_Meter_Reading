from django.contrib import admin
from django.urls import path, include
from .views import login_view, home, signup, uploadimg
from . import views

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('home/', home, name='home'),
    path('uploadimg/', uploadimg, name='uploadimg'),
]
