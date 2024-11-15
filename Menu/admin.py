from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Menu
 
class MenuResource(resources.ModelResource):
    class Meta:
        model = Menu
      
 
class MenuAdmin(ImportExportModelAdmin):
    resource_class = MenuResource  
 
admin.site.register(Menu, MenuAdmin)
