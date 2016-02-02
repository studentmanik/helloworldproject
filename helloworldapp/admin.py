from django.contrib import admin

# Register your models here.
from .models import Poll,Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class PollmodelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","pub_date"]
    inlines = [ChoiceInline]
    search_fields = ['question']
admin.site.register(Poll,PollmodelAdmin)
admin.site.register(Choice)