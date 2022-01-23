from django.contrib import admin

from .models import User, Traveler, ItemDefinition, Node

admin.site.register(User)
admin.site.register(Traveler)
admin.site.register(ItemDefinition)
admin.site.register(Node)