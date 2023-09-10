from django.contrib import admin
from .models import Employer, Store, Product
# Register your models here.





class EmployerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age')
    list_filter = ('first_name', 'age')

    fieldsets = (
        ('name', {
            'fields': ('first_name', 'last_name')
        }),
    )

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'employer')
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'display_store')
    
    



admin.site.register(Employer, EmployerAdmin)