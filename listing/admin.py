from django.contrib import admin
from .models import listingCat
# Register your models here.
@admin.register(listingCat)
class listingCatModelAdmin(admin.ModelAdmin):
    list_display= ('name','slug')