from django.conf.urls import url, include
from django.views.generic import ListView, DetailView #we are no longer using views.py to return template view, but the generic view ListView
from search.models import SearchResult
from .views import SubcategoryResultView, SearchresultView

urlpatterns = [
    #since we arrived here from /search/ in 'website1/urls.py', the pattern we're now looking for is empty string
    url(r'^$', ListView.as_view(queryset=SearchResult.objects.all().order_by("-ConsolidatedRating")[:], #order by descending 'Rating', first 5 results
        template_name="search/SearchResult.html"), name='searchlist'),

    url(r'(?P<key>\d+)/$', SubcategoryResultView.as_view(), name='search'),

    url(r'searchresult/(?P<pk>\d+)', SearchresultView.as_view(), name='searchresult')
]