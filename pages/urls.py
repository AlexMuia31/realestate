from django.urls import path
from .views import search, index

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('search/', search.as_view(), name='search'),
]
