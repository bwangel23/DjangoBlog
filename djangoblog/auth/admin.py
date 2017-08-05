from django.contrib import admin
from .models import UserMeta


# Register your models here.
@admin.register(UserMeta)
class UserMetaAdmin(admin.ModelAdmin):
    pass
