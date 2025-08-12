from django.contrib import admin
from .models import Predstava, Calendar, Comment, Like, PriceItem, Reservation

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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('predstava', 'user', 'approved', 'created_at')
    list_filter = ('approved', 'created_at', 'predstava')
    search_fields = ('text', 'user__username', 'predstava__title')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, f"Odobreno: {updated} komentara")
    approve_comments.short_description = "Odobri odabrane komentare"


admin.site.register(Like)  


@admin.register(PriceItem)
class PriceItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_active', 'display_order')
    list_editable = ('price', 'is_active', 'display_order')
    search_fields = ('name', 'description')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'predstava', 'quantity', 'status', 'created_at')
    list_filter = ('status', 'predstava', 'created_at')
    search_fields = ('name', 'email', 'predstava__title')
    autocomplete_fields = ('predstava',)
