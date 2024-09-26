from django import forms
from .models import User, Realtor
from django.contrib.auth.forms import UserCreationForm



class RealtorSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_realtor = True
        if commit:
            user.save()
            Realtor.objects.create(user=user)
        return user







