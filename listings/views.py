from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Location, Feature, Property
from .forms import LocationForm, PropertyForm, FeatureForm


# Index or home page
def index(request):
    # Get the featured properties
    featured_properties = Property.objects.filter(is_featured=True)[:3]

    return render(request, 'listings/spacehunt.html', {'featured_properties': featured_properties})



# List Property
class PropertyList(ListView):
    model = Property
    template_name = 'listings/property_list.html'
    context_object_name = 'properties'

    def get_queryset(self):
        return super().get_queryset().filter(publish='published')

  

# Create Porperty
class CreatePropertyView(CreateView):
    model = Property
    form_class = PropertyForm
    template_name = 'listings/add_listing.html'
    success_url = reverse_lazy('listings:property_list') 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location_form'] = LocationForm()
        context['features_form'] = FeatureForm()
        return context
    
    def form_valid(self, form):
        location_form = LocationForm(self.request.POST)
        feature_form = FeatureForm(self.request.POST)
        if location_form.is_valid() and feature_form.is_valid():
            self.object = form.save()
            location = location_form.save()
            features = feature_form.save()
            self.object.location = location
            self.object.feature = features
            self.object.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)


# Property Details
class PropertyDetail(DetailView):
    model = Property
    template_name = 'listings/property_detail.html'
    context_object_name = 'property'
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property_detail_url'] = reverse_lazy('listings:property_detail', args=[self.object.pk])
        return context


# Update  property
class UpdateProperty(UpdateView):
    model = Property
    form_class = PropertyForm
    template_name = 'listings/update_property.html'
    success_url = reverse_lazy('listings:property_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['location_form'] = LocationForm(instance=self.object.location)
        context['feature_form'] = FeatureForm(instance=self.object.features)
        return context

    def form_valid(self, form):
        location_form = LocationForm(self.request.POST, instance=self.object.location)
        feature_form = FeatureForm(self.request.POST, instance=self.object.features)
        if location_form.is_valid() and feature_form.is_valid():
            self.object = form.save()
            location = location_form.save()
            feature = feature_form.save()
            self.object.location = location
            self.object.feature = feature
            self.object.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)



# Delete property
class PropertyDelete(DeleteView):
    model = Property
    success_url = reverse_lazy('listings:property_list')  # Redirect to the property list view
    template_name = 'listings/property_delete.html'



class PropertySearchView(ListView):
    model = Property
    template_name = 'listings/property_search.html'
    context_object_name = 'properties'
