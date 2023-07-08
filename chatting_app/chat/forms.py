from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    age = forms.IntegerField()
    image = forms.ImageField()
    name = forms.CharField(max_length=20)


class SignupForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())


class ChatDataForm(forms.Form):
    msg = forms.CharField(max_length=254)
    image = forms.ImageField()
