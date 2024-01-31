from django.shortcuts import render, redirect, HttpResponseRedirect

from accounts.decorators import admin_only, allowed_users, unauthenticated_user
from .models import *
from .forms import *
from .filters import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


# Create your views here.
@unauthenticated_user
def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("accueil")

    return render(request, "accounts/loginpage.html")


@login_required(login_url="loginpage")
def deconnexion(request):
    logout(request)
    return redirect("loginpage")


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="client")
            user.groups.add(group)
            messages.success(request, "compte creer")
            return redirect("accueil")

    return render(request, "accounts/register.html", {"form": form})


@login_required(login_url="loginpage")
@admin_only
def accueil(request):
    clients = Client.objects.all()
    commandes = Commande.objects.all()
    produits = Produit.objects.all()

    totalclients = clients.count()
    totalcommandes = commandes.count()
    totalproduits = produits.count()

    context = {
        "clients": clients,
        "commandes": commandes,
        "totalclients": totalclients,
        "totalcommandes": totalcommandes,
        "totalproduits": totalproduits,
    }
    print(clients)
    return render(request, "accounts/accueil.html", context)


@login_required(login_url="loginpage")
def user_page(request):
    commandes = request.user.client.commande_set.all()

    return render(request, "accounts/user_page.html", {"commandes": commandes})


@login_required(login_url="loginpage")
def produit(request):
    produits = Produit.objects.all()
    return render(request, "accounts/produit.html", {"produits": produits})


@login_required(login_url="loginpage")
def accountsettings(request):
    form = ClientForm(instance=request.user.client)
    if request.method == "POST":
        form = ClientForm(request.POST, request.FILES, instance=request.user.client)
        if form.is_valid():
            form.save()

    return render(request, "accounts/accountsettings.html", {"form": form})


@login_required(login_url="loginpage")
def client(request, pk_test):
    client = Client.objects.get(id=pk_test)
    commandes = client.commande_set.all()
    totalcommande = commandes.count()

    myfilter = CommandeFilter(request.GET, queryset=commandes)
    commandes = myfilter.qs
    context = {
        "client": client,
        "commandes": commandes,
        "totalcommande": totalcommande,
        "myfilter": myfilter,
    }

    return render(request, "accounts/client.html", context)


@login_required(login_url="loginpage")
def create_commande(request, pk):
    client = Client.objects.get(id=pk)

    form = CreateCommandeForm(initial={"client": client})

    if request.method == "POST":
        form = CreateCommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "accounts/create_commande.html", context)


@login_required(login_url="loginpage")
def update_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    form = CreateCommandeForm(instance=commande)

    if request.method == "POST":
        form = CreateCommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "accounts/create_commande.html", context)


@login_required(login_url="loginpage")
def delete_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    form = CreateCommandeForm(instance=commande)

    if request.method == "POST":
        commande.delete()
        return redirect("/")

    context = {"commande": commande}
    return render(request, "accounts/delete_commande.html", context)
