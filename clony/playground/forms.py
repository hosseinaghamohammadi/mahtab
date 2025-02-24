from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import get_user_model
from django import forms
from .models import Student, Project


class SignUpFrom(UserCreationForm):
    password1 = forms.CharField(
            label='گذرواژه',
            strip=False,
            widget=forms.PasswordInput(attrs={
                'dir': 'ltr'
            })
        )
    password2 = forms.CharField(
            label='تکرار گذرواژه',
            strip=False,
            widget = forms.PasswordInput(attrs={
                'dir': 'ltr'
            })
        )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
                'username',
            )
        labels = {
                'username': 'شماره‌ی تلفن همراه',
            }
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None
        self.fields['username'].widget.attrs = {'dir': 'ltr', 'placeholder': '۰۹*********'}
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit)
        user.save()
        student = Student(user=user)
        student.save()

        return user


class LogInForm(AuthenticationForm):
    password = forms.CharField(
        label='گذرواژه',
        strip=False,
        widget=forms.PasswordInput(attrs={
            'dir': 'ltr',
            'data-toggle': 'password',
        })
    )
    class Meta:
        model = get_user_model()
        fields = ('username')

    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'شماره‌ی تلفن همراه'
        self.fields['username'].widget.attrs = {'dir': 'ltr'}


class addProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'link', 'is_private']

    def __init__(self, *args, **kwargs):
        super(addProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'نام پروژه'
        self.fields['name'].widget.attrs = {'dir': 'rtl'}
        self.fields['name'].required = False
        self.fields['link'].label = 'لینک پروژه'
        self.fields['link'].widget.attrs = {'dir': 'rtl'}
        self.fields['link'].required = True
        self.fields['is_private'].label = 'اگر تیک زیر فعال باشد، فقط شما می‌توانید این پروژه را ببینید.'
        self.fields['is_private'].widget.attrs = {'dir': 'rtl'}
        self.fields['is_private'].required = False

class EditProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'link', 'is_private']

    def __init__(self, *args, **kwargs):
        super(EditProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'نام پروژه'
        self.fields['name'].widget.attrs = {'dir': 'rtl'}
        self.fields['name'].required = False
        self.fields['link'].label = 'لینک پروژه'
        self.fields['link'].widget.attrs = {'dir': 'rtl'}
        self.fields['link'].required = True
        self.fields['is_private'].label = 'اگر تیک زیر فعال باشد، فقط شما می‌توانید این پروژه را ببینید.'
        self.fields['is_private'].widget.attrs = {'dir': 'rtl'}
        self.fields['is_private'].required = False