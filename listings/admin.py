from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Location, Property, Feature, Review

class LocationAdmin(admin.ModelAdmin):
   list_display = ('country', 'street', 'city', 'state', 'postal_code')  # Update 'zipcode' to 'postal_code'
   list_filter = ('country', 'city')

admin.site.register(Location, LocationAdmin)


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
      list_display = ('name', 'property_type', 'price', 'status', 'bedrooms','created_date')
      list_filter = ('price', 'name', 'status')
      
      fieldsets = (
        ('Listing Information', {
            'fields': ('id','name', 'property_type','description','price','location','status'),
        }),
        ('Listing Features', {
            'fields': ('photo','bedrooms','bathrooms','garage','total_area', 'features','video_url'),
            'classes': ('collapse',),
        }),

        ('Realtor Info', {
            'fields': ('realtor','publish','is_featured', ),
            'classes': ('collapse',),
        }),
       )
      

@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('wifi', 'personal_safe', 'minibar', 'refrigerator', 'electronic_key_card_access','air_conditioning','heating','pool','equipped_Kitchen','washing_machine')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
     list_display = ('property', 'rating', 'user')
     list_filter = ('property', 'created_at')