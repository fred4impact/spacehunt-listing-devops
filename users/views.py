from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Realtor
from django.contrib.auth.views import LoginView
from listings.models import Property
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from .forms import RealtorSignUpForm



class RealtorSignUp(View):
    def get(self, request):
        form = RealtorSignUpForm()
        return render(request, 'users/signup.html', {'form': form})

    def post(self, request):
        form = RealtorSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('realtor_dashboard')

        return render(request, 'users/signup.html', {'form': form})


def toggle_realtor_activation(request, pk):
    # Get the realtor object
    realtor = get_object_or_404(Realtor, id=pk)

    # Get the superuser performing the action (assuming it's the currently logged-in user)
    user_id = request.user.id

    # Check if the user is a superuser and toggle the activation
    User = get_user_model()
    if User.objects.filter(pk=user_id, is_superuser=True).exists():
        realtor.toggle_activation(user_id)
    else:
        raise PermissionDenied("Only superusers can toggle realtor activation.")

    return render(request, 'realtor/activation_success.html')














class CustomLoginView(LoginView):
    template_name = 'users/signin.html'
    redirect_authenticated_user = True


@login_required(login_url='login')
def realtor_dashboard(request):
    user = request.user
    properties = Property.objects.filter(realtor=user)

    return render(request, 'dashboard/dashboard.html', {'properties': properties})
