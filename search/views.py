from django.shortcuts import render
from django.views.generic import ListView, DetailView
from search.models import SearchResult

class SubcategoryResultView(ListView):
    model = SearchResult
    template_name = 'search/SubcategoryResult.html'
    context_object_name = 'subcategory_list'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        return qs.filter(subcategory=self.kwargs['key']).order_by("id")

        # qs = super().get_queryset()
        # # filter by a variable captured from url, for example
        # return qs.filter(name__startswith=self.kwargs.name)

        ## Call the base implementation first to get a context
        # context = super(PublisherDetailView, self).get_context_data(**kwargs)
        ## Add in a QuerySet of all the books
        # context['book_list'] = Book.objects.all()
        # return context

#
class SearchresultView(DetailView):
    model = SearchResult
    template_name = 'search/SearchResult.html'
    context_object_name = 'searchresult'
