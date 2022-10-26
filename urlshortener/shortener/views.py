from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from .models import url_Model
from .forms import url_Form
from .zip import get_zipped
# Create your views here.
def home(Request):
    return render(Request, 'home.html')

def short(Request):
    form = url_Form()
    context = {'form': form}
    return render(Request, 'short.html', context)

def res(Request):
    if(Request.method=='POST'):
        form = url_Form(Request.POST)
        a=long=''
        if form.is_valid():
            if not(url_Model.objects.filter(long_url=form.cleaned_data['long_url']).exists()):
                entry = form.save(commit=False)
                long = entry.long_url
                temp = get_zipped()
                while url_Model.objects.filter(pk=temp).exists():
                    temp = get_zipped()
                entry.short_url = temp
                a = 'http://127.0.0.1:8000/url/'+entry.short_url
                entry.save()
            else:
                short_url=url_Model.objects.get(long_url=form.cleaned_data['long_url'])
                a='http://127.0.0.1:8000/url/'+short_url.short_url
                long=short_url.long_url
        context = {'long':long, 'short': a}
        
    return render(Request, 'result.html', context)

def direction(Request, key):
    x = url_Model.objects.get(short_url=key)
    return redirect(x.long_url)
