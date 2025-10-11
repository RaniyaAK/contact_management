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


def manage_contacts(request):
    contacts = Profile.objects.select_related('user').all()
    return render(request, 'manage_contacts.html', {'contacts': contacts})

def manage_users(request):
    users = User.objects.all()
    return render(request, 'admin_manage_users.html', {'users': users})



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
    return render(request, "edit.html", {"contact": contact,"cancel_url": "contacts" })



@login_required
def delete(request, id):
    contact = get_object_or_404(Profile, id=id)
    if request.method == "POST":
        contact.delete()
        return redirect("contacts")
    return render(request, "delete_confirm.html", {"contact": contact,"cancel_url": "contacts"})


def manage_users(request):
    users = User.objects.all()
    return render(request, 'manage_users.html', {
        'users': users,
        'cancel_url': 'manage_users',  # redirect if Cancel is clicked
    })


@login_required
def manage_users_delete(request,id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        user.delete()
        return redirect("manage_users")
    return render(request, "manage_users_delete.html", {"user": user})

@login_required
def manage_users_edit(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == "POST":
        user.username = request.POST.get("name")
        User.phone = request.POST.get("phone")
        user.email = request.POST.get("email")
        user.save()
        return redirect("manage_users")
    return render(request, "manage_users_edit.html", {"user": user})

@login_required
def manage_contacts(request):
    contacts = Profile.objects.select_related('user').all()
    return render(request, 'manage_contacts.html', {'contacts': contacts})


@login_required
def manage_contacts_edit(request, id):
    contact = get_object_or_404(Profile, id=id)
    if request.method == "POST":
        contact.name = request.POST.get("name")
        contact.phone = request.POST.get("phone")
        contact.email = request.POST.get("email")
        contact.save()
        return redirect("manage_contacts")
    return render(request, "manage_contacts_edit.html", {"contact": contact,"cancel_url": "contacts" })


@login_required
def manage_contacts_delete(request, id):
    contact = get_object_or_404(Profile, id=id)
    if request.method == "POST":
        contact.delete()
        return redirect("manage_contacts")
    return render(request, "manage_contacts_delete.html", {"contact": contact,"cancel_url": "contacts"})



@login_required
def admin_dashboard(request):
    users_count =  User.objects.filter(is_superuser=False).count()
    contacts_count = Profile.objects.count()
    users_count_with_admin = User.objects.count() 
    return render(request, 'admin_dashboard.html',{
        'users_count': users_count,
        'contacts_count': contacts_count,
        'users_count_with_admin':users_count_with_admin
    })


def user_logout(request):
    logout(request)
    return redirect('login')
