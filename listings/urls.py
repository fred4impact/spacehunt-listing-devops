from django.urls import path
from listings.views import index
from . import views

app_name = 'listings'


urlpatterns = [
    path('', index, name='index'),

    path('all', views.PropertyList.as_view(), name='property_list'),

    path('create/', views.CreatePropertyView.as_view(), name='create_property'),

    path('<str:pk>/', views.PropertyDetail.as_view(), name='property_detail'),

    path('<str:pk>/update/', views.UpdateProperty.as_view(), name='property_update'),

    path('<str:pk>/delete/', views.PropertyDelete.as_view(), name='property_delete'),

    path('search/', views.PropertySearchView.as_view(), name='property_search'),
]