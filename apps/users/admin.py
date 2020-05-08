from django.contrib import admin

# Register your models here.
# from apps.users.models import UserProfile
# class UserProfileAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(UserProfile,UserProfileAdmin)
from django.contrib.auth.admin import UserAdmin
from apps.users.models import UserProfile
#优化显示
admin.site.register(UserProfile,UserAdmin)