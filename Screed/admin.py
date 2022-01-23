from django.contrib import admin

from .models import User, Traveler, ItemDefinition, Item, Node, Edit, Choice, Reward

admin.site.register(User)
admin.site.register(Traveler)
admin.site.register(ItemDefinition)
admin.site.register(Item)
admin.site.register(Node)
admin.site.register(Edit)
admin.site.register(Choice)
admin.site.register(Reward)