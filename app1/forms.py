from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
