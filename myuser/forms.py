from django import forms
from myuser.models import MyUser


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    
    
class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=25) 
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = MyUser
        fields = ["displayname", "age", "homepage"]