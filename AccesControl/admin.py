from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserP

# Register your models here.
class UserPAdmin(UserAdmin):
    readonly_fields = ['id']

admin.site.register(UserP, UserPAdmin)