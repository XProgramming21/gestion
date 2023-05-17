from . import views
from django.urls import path


urlpatterns = [

    path('loginpage/', views.loginpage, name="loginpage"),
    path('register/', views.register, name="register"),
    path('deconnexion/', views.deconnexion, name="deconnexion"),


    path('', views.accueil, name="accueil"),
    path('user/', views.user_page, name="user_page"),
    path('account/', views.accountsettings, name="accountsettings"),
    path('produit/', views.produit, name="produit"),
    path('client/<str:pk_test>/', views.client, name="client"),
    path('create_commande/<str:pk>/', views.create_commande, name="create_commande"),
    path('update_commande/<str:pk>/', views.update_commande, name="update_commande"),
    path('delete_commande/<str:pk>/', views.delete_commande, name="delete_commande"),
]
