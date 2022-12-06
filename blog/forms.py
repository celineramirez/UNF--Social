from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Hidden
from django import forms
from datetime import date, datetime
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

    published_date = forms.DateField(initial=datetime.now())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["author"].initial = user
        self.fields['published_date'].widget.attrs['readonly'] = True

    class Meta:
        model = Post
        fields = ('author', 'thumbnail', 'title', 'text', 'event_date', 'published_date', 'tag')
        widgets = {'author': forms.HiddenInput(), 'published_date': forms.HiddenInput()}



