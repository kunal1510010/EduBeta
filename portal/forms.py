from django import forms


class UserForm(forms.Form):
    user_name = forms.CharField(max_length=20)
    email_id = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    widgets = {
        'password': forms.PasswordInput(),
    }


class LoginForm(forms.Form):
    email_id = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    widgets = {
        'password': forms.PasswordInput(),
    }


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Supported Formats',
        help_text='CSV'
    )
