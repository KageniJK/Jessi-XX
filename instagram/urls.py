from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'home'),
    url('^profile/',views.profile, name='profile'),
    url('^search_results/',views.search_results,name='search_results'),
]