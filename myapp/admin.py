from django.contrib import admin
from myapp.models import service
# Register your models here.
class serviceadmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des')
    
admin.site.register(service,serviceadmin)


