from django.contrib import admin
from .models import my_team, Place  # Make sure to import your models

# Register your models with the admin site
admin.site.register(my_team)
admin.site.register(Place)
