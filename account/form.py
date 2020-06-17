from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username = forms.CharField(label=' 帳號', max_length=50)
    password1 = forms.CharField(label=' 密碼 ', widget=forms.PasswordInput)
    password2 = forms.CharField(label='確認密碼', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 6:
            raise forms.ValidationError("帳號太短至少要6個字")
        elif len(username) > 50:
            raise forms.ValidationError("帳號太長")
        else:
            filter_result = User.objects.filter(username__exact=username)
            if len(filter_result) > 0:
                raise forms.ValidationError("帳號已存在")
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if len(password1) < 6:
            raise forms.ValidationError("密碼太短至少要6個字")
        elif len(password1) > 20:
            raise forms.ValidationError("密碼太長")
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("密碼不正確 請重新輸入")

        return password2


class LoginForm(forms.Form):
    username = forms.CharField(label='帳號', max_length=50)
    password = forms.CharField(label='密碼', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        filter_result = User.objects.filter(username__exact=username)
        if not filter_result:
            raise forms.ValidationError("用戶名不存在")
        return username