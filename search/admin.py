from django.contrib import admin

from search.models import  *

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(SearchResult)
admin.site.register(UserRatings)