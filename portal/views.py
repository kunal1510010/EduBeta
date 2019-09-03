from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from .forms import DocumentForm
from .models import Document


def index(request):
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            print(Document.objects.all())
            return HttpResponseRedirect('')
    context = {
        'form': form,
        'title': 'Form Django is stupid',
    }
    return render(request, 'Main.html', context)
