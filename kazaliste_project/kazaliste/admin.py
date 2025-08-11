from django.contrib import admin
from .models import Predstava, Calendar

# Register your models here.


@admin.register(Predstava)
class PredstavaAdmin(admin.ModelAdmin):
    list_display = ("title", "duration_minutes", "age_min", "is_active")
    list_filter = ("is_active", "age_min")
    search_fields = ("title", "description")


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ("predstava", "date", "time", "dvorana", "is_published")
    list_filter = ("is_published","date")
    search_fields = ("predstava__title", "dvorana")
    autocomplete_fields = ("predstava",)