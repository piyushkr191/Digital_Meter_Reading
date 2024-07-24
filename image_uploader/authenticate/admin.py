from django.contrib import admin
# from django.contrib.auth import get_user_model  # Correctly import User model
from .models import Profile, Image  # Import models from your app

# Get the user model
# User = get_user_model()

# Register Profile and Image models
admin.site.register(Profile)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'date']

# Register User model if using a custom model
# try:
#     admin.site.register(User)
# except admin.sites.AlreadyRegistered:
#     pass
