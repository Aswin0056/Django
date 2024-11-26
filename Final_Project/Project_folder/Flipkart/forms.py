from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


###address


from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'full_name',
            'phone_number',
            'address_line1',
            'address_line2',
            'city',
            'state',
            'postal_code',
            'country',
        ]

