from django.urls import path
from .views import about, index

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('about/', about.as_view(), name='about'),
]
