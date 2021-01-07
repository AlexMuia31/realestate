from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import home

# Create your views here.

class index(TemplateView):
    template_name= 'pages/index.html'


class about(ListView):
    model= home
    template_name='pages/singlepage.html'