from django.contrib import admin
from .models import Rig

# Register your models here.
class RigAdmin(admin.ModelAdmin):
    pass

    # inlines = []

admin.site.register(Rig, RigAdmin)