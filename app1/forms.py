from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfile
from django import forms


class ExtendedUserCreationForm(UserCreationForm):
    user: User

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active']

    def save(self, commit=True):
        self.user = super().save(commit=False)
        if commit:
            self.user.save()
        return self.user


class UserProfileForm(ModelForm):
    card_id = forms.CharField(required=True)
    authority = forms.CharField(required=True)
    position = forms.CharField(required=True)

    class Meta:
        model = UserProfile
        fields = ['card_id','authority','position']
