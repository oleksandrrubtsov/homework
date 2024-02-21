from django.contrib import admin
from .models import Category, Notes

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
  list_display = ("title", "text", "reminder","category","created_by")

admin.site.register(Category)
admin.site.register(Notes,NotesAdmin)
