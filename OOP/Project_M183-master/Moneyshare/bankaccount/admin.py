from django.contrib import admin
from .models import Bankaccoount, Transaktion, Antrag

# Register your models here.
admin.site.register(Bankaccoount)
admin.site.register(Transaktion)
admin.site.register(Antrag)