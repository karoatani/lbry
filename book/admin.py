from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from . import models
from django.db.models import F
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
# Register your models here.

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name',"get_author")
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        query_set = super().get_queryset(request).prefetch_related('author').annotate(author_name=F("author__name"))
        return query_set
    

    def get_author(self,obj):

        url = (
            reverse("admin:author_author_changelist")
            + "?"
            + urlencode({"book_set__id": f"{obj.id}"})
        )
        return format_html('<a href="{}">{} Students</a>', url, obj.author_name)
    
    get_author.short_description = "Authors name"

admin.site.register(models.Category)