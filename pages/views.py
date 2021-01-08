from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import home
from django.db.models import Q

# Create your views here.

class index(TemplateView):
    template_name= 'pages/index.html'


class search(ListView):
    model= home
    template_name='pages/search.html'

    def get_queryset(self):
        query= self.request.GET.get('q')
        object_list= home.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return object_list