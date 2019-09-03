from django import forms


class UploadFileForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    file = forms.FileField(required=False)


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )
