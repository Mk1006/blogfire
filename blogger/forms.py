from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from pip._vendor.pkg_resources import require


class RegistrationForm(UserCreationForm):
    mobile_no = forms.CharField()
    email_id = forms.CharField()
    
    class Meta:
        model = User
        fields = (
            'username',
            'mobile_no',
            'email_id',
            'password1',
            'password2',
         )
        
        

class EditProfileForm(UserChangeForm):
    email_id = forms.CharField(required=False)
    birth_date = forms.DateField(required=False)
    home_town = forms.CharField(required=False)
    bio = forms.CharField(required=False)
    hobbies = forms.CharField(required=False)
    
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name', 
            'email_id', 
            #'profile_pic',
            'birth_date', 
            'home_town',
            'bio',
            'hobbies',
            'password',
         )
    
    
    
    