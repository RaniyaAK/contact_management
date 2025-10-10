from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserForm
from .models import Profile
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard' if user.is_superuser else 'contacts')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def contacts(request):
    x = Profile.objects.filter(user=request.user)  # x instead of contacts
    return render(request, 'contacts.html', {'x': x})

@login_required
def add_contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        Profile.objects.create(user=request.user,name=name, phone=phone, email=email)
        return redirect('contacts')
    return render(request, 'add_contacts.html')

@login_required
def contact(request, id):
    contact = get_object_or_404(Profile, id=id)
    return render(request, 'contact.html', {'contact': contact})


@login_required
def edit(request, id):
    contact = get_object_or_404(Profile, id=id)
    if request.method == "POST":
        contact.name = request.POST.get("name")
        contact.phone = request.POST.get("phone")
        contact.email = request.POST.get("email")
        contact.save()
        return redirect("contacts")
    return render(request, "edit.html", {"contact": contact})

@login_required
def delete(request, id):
    contact = get_object_or_404(Profile, id=id)
    if request.method == "POST":
        contact.delete()
        return redirect("contacts")
    return render(request, "delete_confirm.html", {"contact": contact})


# @login_required
# def user_dashboard(request):
#     return render(request, 'user_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('login')
