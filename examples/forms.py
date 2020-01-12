from django import forms
from bootstrap_modal_forms.forms import BSModalForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Device, Customer, CustomerDevice
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class DeviceForm(BSModalForm):
    publication_date = forms.DateField(
        error_messages={'invalid': 'Enter a valid date in YYYY-MM-DD format.'}
    )

    class Meta:
        model = Device
        exclude = ['timestamp']


class CustomerForm(BSModalForm):
    email = forms.EmailField(
        error_messages={'invalid': 'Enter a valid date in XXX@.com format.'}
    )

    class Meta:
        model = Customer
        exclude = ['users_name']


class CustomerDeviceForm(BSModalForm):
    class Meta:
        model = CustomerDevice
        exclude = ['device_name']


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: #2a3747;',
                'placeholder': 'Username'
            }), label='')
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'style': 'border-color: #2a3747;',
                'placeholder': 'Password'
            }), label='')

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: #2a3747;',
                'placeholder': 'Username'
            }), label='')
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'style': 'border-color: #2a3747;',
            'placeholder': 'Email'
        }), label='')
    email2 = forms.EmailField(widget=forms.TextInput(
        attrs={
            'style': 'border-color: #2a3747;',
            'placeholder': 'Confirm Email'
        }), label='')
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'style': 'border-color: #2a3747;',
            'placeholder': 'Password'
        }), label='')

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("Emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError(
                "This email has already been registered")
        return super(UserRegisterForm, self).clean(*args, **kwargs)


class CommandForm(BSModalForm):
    command = forms.CharField(label='Command to execute')
    class Meta:
        model = Device
        exclude = ['timestamp', 'publication_date', 'device_type']


# class CmdForm(forms.Form):
#     command = forms.CharField(label='Command to execute')
