from django.shortcuts import render
from django.http import HttpResponse
from .forms import  ContactForm, SnippetForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)   #passes data user provided

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            print(name, email)
    form = ContactForm()

    return render(request,'apptwo/form.html',{'form':form})


def snippet_form(request):
     name=''
     body=''
     formone = SnippetForm()
     if request.method == 'POST':
           
        formone = SnippetForm(request.POST)

        if formone.is_valid():
            print('Its successful')
            name = formone.cleaned_data['name']
            body = formone.cleaned_data['body']
        
        # args = {'formone':formone, 'name':name, 'body':body}
    
     return render(request,'apptwo/form.html',{'name':name,'body':body, 'form':formone})


def profile(request):
    # it is to show links using a tag(simplest way)

    return render(request,'apptwo/profile.html')