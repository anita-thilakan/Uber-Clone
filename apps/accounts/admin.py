from django.contrib import admin
from .models import Driver,Rider

# Register your models here.
@admin.register(Rider)
class RiderAdmin(admin.ModelAdmin):
    list_display = ('id','user')

admin.site.register(Driver)
# admin.site.register(Rider)

