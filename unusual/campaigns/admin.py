from django.contrib import admin
import campaigns.models

admin.site.register(campaigns.models.Campaign)
admin.site.register(campaigns.models.Milestone)