from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView
from search.models import Subcategory, Category

def index(request):
    return render(request, 'home/home.html') #we can pass a dictionary as the 3rd parameter which is like passing a model in c#

def contact(request):
    return render(request, 'home/basic.html', {'content': ['If you would like to contact me, please email me', 'shawnpuri199@gmail.com']})

class SubcategoryView(ListView):
    model = Subcategory
    template_name = 'home/subcategory.html'
    context_object_name = 'subcategory_list'

    def get_queryset(self, **kwargs):
        qs = super(SubcategoryView, self).get_queryset()
        self.category = get_object_or_404(Category, id=self.kwargs['pk']) #Get category record filter by ID???
        return qs.filter(category=self.kwargs['pk']).order_by("id")

    def get_context_data(self, **kwargs):
        context = super(SubcategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context

        # qs = super().get_queryset()
        # # filter by a variable captured from url, for example
        # return qs.filter(name__startswith=self.kwargs.name)

        ## Call the base implementation first to get a context
        # context = super(PublisherDetailView, self).get_context_data(**kwargs)
        ## Add in a QuerySet of all the books
        # context['book_list'] = Book.objects.all()
        # return context