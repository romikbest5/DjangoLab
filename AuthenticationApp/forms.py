from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Имя пользователя", max_length=30, widget=forms.TextInput(attrs={"class": "form-control",
                                                                                              "id": "Username"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                                   "id": "Password"}))


class UserRegisterForm(forms.Form):
    username = forms.CharField(label="Имя пользователя", max_length=30, widget=forms.TextInput(attrs={"class": "form-control",
                                                                                              "id": "Username"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                                   "id": "Password"}))
    repeat_password = forms.CharField(label="Повторите пороль", widget=forms.PasswordInput(attrs={"class": "form-control",
                                                                                   "id": "RepeatPassword"}))
