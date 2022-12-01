from django import forms
from datetime import date
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


# Create your forms here.
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'thumbnail', 'title', 'text', 'event_date', 'published_date', 'tag')
        model.published_date = date.today()


