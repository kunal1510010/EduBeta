from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import DocumentForm, UserForm, LoginForm
from .models import Document, UserDetail
from passlib.hash import pbkdf2_sha256
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from . import preprocessing


def data(request, file_name):
    data_head = preprocessing.read(file_name)
    return HttpResponse(data_head)


def dashboard(request):
    if request.session.get('user_id', True):
        documents = Document.objects.filter(user_id=request.session['user_id'])
        form = DocumentForm()
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)

            if form.is_valid():
                new_doc = Document.objects.create(user_id=request.session['user_id'], doc_file=request.FILES['docfile'])
                new_doc.save()
                return HttpResponseRedirect('/dashboard/')
        context = {
            'form': form,
            'documents': documents,
        }
        return render(request, 'Main.html', context)
    else:
        return HttpResponseRedirect('/login/')


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_name_temp = form.cleaned_data["user_name"]
            email_temp = form.cleaned_data["email_id"]
            password_temp = form.cleaned_data["password"]
            enc_password = pbkdf2_sha256.encrypt(password_temp)
            job_obj = UserDetail.objects.create(user_name=user_name_temp, email_id=email_temp, password=enc_password)
            job_obj.save()

            return HttpResponseRedirect("/login/")
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_email_tmp = form.cleaned_data["email_id"]
            password_tmp = form.cleaned_data["password"]
            username_check = UserDetail.objects.get(email_id=user_email_tmp)
            try:
                if pbkdf2_sha256.verify(password_tmp, username_check.password):
                    request.session['user_id'] = username_check.user_id
                    return HttpResponseRedirect('/dashboard/')
                else:
                    messages.error(request, "Password Incorrect")
            except ObjectDoesNotExist:
                messages.error(request, "SignUp First")

    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def index(request):
    return render(request, 'index.html')


def logout(request):
    try:
        del request.session['user_id']
        return HttpResponseRedirect('/login/')
    except:
        print('something wrong')
        return HttpResponseRedirect('/')
