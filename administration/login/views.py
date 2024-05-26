from django.shortcuts import render, redirect 
from django.contrib.auth.forms import UserCreationForm 

# Create your views here.
def login(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mainplatform:list") # redirect to main platform
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", { "form": form })