from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Traveler)
admin.site.register(StatDefinition)
admin.site.register(Stat)
admin.site.register(ItemDefinition)
admin.site.register(Item)
admin.site.register(Node)
admin.site.register(Edit)
admin.site.register(Check)
admin.site.register(Choice)
admin.site.register(Reward)