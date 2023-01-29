from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class Register(forms.ModelForm):
    class Meta:
        models = User
        fields = ['username', 'password']