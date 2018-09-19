from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from search.models import Category, Subcategory

from . import views
from .views import SubcategoryView
#the second parameter tells you which function in views.py to look for (since views is imported above)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'frameworkslist/$', ListView.as_view(queryset=Category.objects.all().order_by("id"),# order by descending 'Name'
                                template_name="home/FrameworksList.html", context_object_name ='category_list'), name='frameworkslist'),
    url(r'frameworkslist/(?P<pk>\d+)$', SubcategoryView.as_view(), name='frameworkslist'), #regex for a primary key of type digit
]
