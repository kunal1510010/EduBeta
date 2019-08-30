from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UploadFileForm


def index(request):
    form = UploadFileForm()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    print(form.as_table())
    return render(request, 'forms.html', {form: form})


def handle_uploaded_file(file):
    with open('uploads/data_file.csv', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

