from django.contrib import admin
from .models import HeaderImage,Product,ProductImage,Size,Color,Category,User,OrderStatus,LaundryService


class LaundryServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'description', 'image')
    list_filter = ('cost',)
    search_fields = ('name', 'description')

admin.site.register(LaundryService, LaundryServiceAdmin)



class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'postal_code')
    search_fields = ('code', 'postal_code')



admin.site.register(User)
admin.site.register(HeaderImage)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(OrderStatus)
