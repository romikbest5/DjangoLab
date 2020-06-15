from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={"class": "form-control",
                                                                                              "id": "Username"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                                   "id": "Password"}))


class UserRegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={"class": "form-control",
                                                                                              "id": "Username"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                                   "id": "Password"}))
    repeat_password = forms.CharField(label="RepeatPassword", widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                                   "id": "RepeatPassword"}))
