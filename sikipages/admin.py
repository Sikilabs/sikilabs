from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import SikiPage

admin.site.register(SikiPage, PageAdmin)