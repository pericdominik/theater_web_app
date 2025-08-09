from django.contrib import admin
from .models import Predstava

# Register your models here.


@admin.register(Predstava)
class PredstavaAdmin(admin.ModelAdmin):
    list_display = ("title", "duration_minutes", "age_min", "is_active")
    list_filter = ("is_active", "age_min")
    search_fields = ("title", "description")