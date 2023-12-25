from django.contrib import admin
from . models import Api_config,wallet
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class Accountinline(admin.StackedInline):
    model = wallet
    can_delete = False
    verbose_name_plural = "wallet"

class cusomizeuseradmin(UserAdmin):
    inlines = (Accountinline, )

class postadmin(admin.ModelAdmin):
    list_display = ('user','balance')    
admin.site.register(wallet,postadmin)


admin.site.unregister(User) 
admin.site.register(User, cusomizeuseradmin,  )
admin.site.register(Api_config)

