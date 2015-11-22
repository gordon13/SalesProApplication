from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import Property, UserProfile, Buyer, Seller

admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [ UserProfileInline]
    #list_display = ('username', 'email', 'last_login', 'is_superuser')

admin.site.register(User, UserProfileAdmin)
admin.site.register(Property)
admin.site.register(Buyer)
admin.site.register(Seller)