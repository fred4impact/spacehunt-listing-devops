from django import forms
from .models import Property
from .models import Property, Location, Feature
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Property, Review


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'  



class FeatureForm(forms.ModelForm):
    class Meta:
        model = Feature
        fields = '__all__'  



class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['name', 'description', 'property_type', 'location', 'photo', 'price',
                  'bedrooms', 'bathrooms', 'garage', 'total_area', 'status', 'is_featured',
                  'features', 'realtor', 'video_url', 'publish']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6'),
                Column('property_type', css_class='form-group col-md-6'),
            ),
            'description',
            Row(
                Column('location', css_class='form-group col-md-6'),
                Column('photo', css_class='form-group col-md-6'),
            ),
            'price',
            Row(
                Column('bedrooms', css_class='form-group col-md-4'),
                Column('bathrooms', css_class='form-group col-md-4'),
                Column('garage', css_class='form-group col-md-4'),
            ),
            'total_area',
            'status',
            'is_featured',
            'features',
            'realtor',
            'video_url',
            'publish',
            Submit('submit', 'Save')
        )
        
      # Hide the 'features' and 'location' fields
        self.fields['features'].widget = forms.HiddenInput()
        self.fields['location'].widget = forms.HiddenInput()



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']