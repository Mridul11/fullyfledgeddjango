from django import forms 
from django.contrib.auth import authenticate, login

class ContactForm(forms.Form):
    fullname = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'one' not in email:
            raise forms.ValidationError("Email is must be from one!")
        return email 

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput, max_length=32)
    confirm_password = forms.CharField(widget=forms.PasswordInput, max_length=32)

    def clean(self):
        data = self.cleaned_data
        p1 = self.cleaned_data.get('password')
        p2 = self.cleaned_data.get('confirm_password')
        if p1 != p2 : 
            raise forms.ValidationError("Password do not match!")
        return data 
            



