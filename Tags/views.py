from django.shortcuts import render
from django.http import request
from .forms import TagForm
from .models import Tag

def tag_view(request):
    form = TagForm(request.POST or None)
    context = {"form" : form}
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        
    return render(request, "tags/home.html", context)
