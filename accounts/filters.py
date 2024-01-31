import django_filters

from .models import *


class CommandeFilter(django_filters.FilterSet):
    class Meta:
        model = Commande
        fields = "__all__"
        exclude = ["client", "date"]
