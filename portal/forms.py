from django import forms


class UploadFileForm(forms.Form):

    first_name = forms.CharField(required=True, label="Title", max_length=20,
                                 widget=forms.TextInput(attrs={'placeholder': 'File Name'}))
    file = forms.FileField()
