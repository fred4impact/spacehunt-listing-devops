from django.conf import settings
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField


class Location(models.Model):
    country = models.CharField('Country',max_length=100)
    street = models.CharField('Street',max_length=100)
    city = models.CharField('City',max_length=100)
    state = models.CharField('State',max_length=100)
    postal_code =models.CharField('Postal code', max_length=100, blank =True)
   

    def __str__(self):
        return f"{self.country}, {self.street}, {self.city}, {self.state}, {self.postal_code}"



class Property(models.Model):

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    PROPERTY_TYPES = (
            ('deluxe_houses', 'Deluxe Houses'),
            ('bungalow', 'Bungalow'),
            ('modern_flats', 'Modern Flats'),
            ('apartments', 'Apartments'),
            ('industrial', 'Industrial'),
            ('condos', 'Condos'),
            ('offices', 'Offices'),
            ('retails ', 'Retails'),
            ('villas', 'Villas'),
            ('shop', 'Shop'),
    )

    PROPERTY_STATUS = (
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
    )
     # new changes 
    id = ShortUUIDField(
        length=12,
        max_length=40,
        prefix="spc",
        alphabet="abcdefg123456",
        primary_key=True)
    name = models.CharField('Property Name',max_length=100)
    description = models.TextField('About Your Property',)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)

    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField('Add Property Image',upload_to='property_images/', default='default_image.jpg')

    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
   
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default=0)
    total_area = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    status = models.CharField(max_length=4, choices=PROPERTY_STATUS)
   
    is_featured = models.BooleanField(default=False)
    features = models.OneToOneField('Feature', on_delete=models.CASCADE, blank=True, null=True )  # Add OneToOneField
   
    realtor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video_url = models.URLField('Property Video Link',blank=True)

    publish = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')  # newly added
    created_date = models.DateTimeField(auto_now=True) # newly added


    class Meta:
        verbose_name_plural = 'properties'
        ordering=['name'] 

    def is_visible(self):
            return self.publish == 'published'    

    def __str__(self):
        return self.name




class Feature(models.Model):
    wifi = models.BooleanField(default=False, verbose_name='Wifi')

    personal_safe = models.BooleanField(default=False, verbose_name='Personal Safe')
    minibar = models.BooleanField(default=False, verbose_name='Mini Bar')

    refrigerator = models.BooleanField(default=False, verbose_name='Refridgerator')
    electronic_key_card_access = models.BooleanField(default=False, verbose_name='Electric Keys/Card Access')

    air_conditioning = models.BooleanField(default=False, verbose_name='Air conditioning')

    heating = models.BooleanField(default=False, verbose_name='Heating')

    pool = models.BooleanField(default=False, verbose_name='Pool')

    equipped_Kitchen = models.BooleanField(default=False, verbose_name= 'Equipped Kitchen')

    washing_machine = models.BooleanField(default=False, verbose_name= 'Washing machine')

    class Meta:
            verbose_name_plural = 'features'

    def get_selected_features(self):
        selected_features = []
        if self.wifi:
            selected_features.append('wifi')
        if self.personal_safe:
            selected_features.append('Personal Safe')
        if self.minibar:
            selected_features.append('Mini Bar')
        if self.refrigerator:
            selected_features.append('Refridgerator')
        if self.electronic_key_card_access:
            selected_features.append('Electric Keys/Card Access')
        if self.air_conditioning:
            selected_features.append('Air conditioning')
        if self.heating:
            selected_features.append('Heating')
        if self.pool:
            selected_features.append('Pool')
        if self.equipped_Kitchen:
            selected_features.append('Equipped Kitchen')
       	if self.washing_machine:
            selected_features.append('Washing machine')
										

        return ', '.join(selected_features)


    def __str__(self):
        return self.get_selected_features()


class Enquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message= models.TextField(blank=True, null=True)
    contact_number = models.CharField('Phone Number', max_length=50, blank=True, null=True )
    preferred_date =models.DateField()

    # Add any additional fields relevant to the viewing booking

    def __str__(self):
        return f"{self.property} - {self.name}"



class Review(models.Model):
        
        RATING_CHOICES = (
            (1, '1 Star'),
            (2, '2 Stars'),
            (3, '3 Stars'),
            (4, '4 Stars'),
            (5, '5 Stars'),
        )

        property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reviews')
        user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        rating = models.IntegerField(choices=RATING_CHOICES, default=None)
        comment = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"Review for {self.property} by {self.user}"


        class Meta:
            verbose_name_plural = 'Property Reviews'


        def get_rating(self):
            return self.rating
