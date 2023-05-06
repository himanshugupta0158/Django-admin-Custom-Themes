from django.contrib import admin
from .models import *

@admin.register(Individual)
class IndividualAdmin(admin.ModelAdmin):
    search_fields = ['individual_id', 'ghana_card_id', 'name_of_individual', 'status']
