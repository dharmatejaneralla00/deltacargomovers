from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.clientlist)
admin.site.register(models.UserLogins)
admin.site.register(models.Destination)