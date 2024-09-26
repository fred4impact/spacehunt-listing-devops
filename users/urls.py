from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RealtorSignUp,realtor_dashboard, CustomLoginView, toggle_realtor_activation


urlpatterns = [
    path('signup/', RealtorSignUp.as_view(), name='realtor_signup'),
    
#     path('signin/', auth_views.LoginView.as_view(template_name='users/signin.html', redirect_authenticated_user=True), name='login'),

    path('login/', CustomLoginView.as_view(), name='login'),

    path('signout/', auth_views.LogoutView.as_view(), name='logout'),

    # this view is use to activate the realtor
    path('dashboard/<int:pk>/toggle_activation/', toggle_realtor_activation, name='toggle_realtor_activation'),
    
    path('dashboard/', realtor_dashboard, name='realtor_dashboard'),

]