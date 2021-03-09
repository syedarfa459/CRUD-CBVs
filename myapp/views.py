from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Kite


# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')


class KiteListView(ListView):
    model = Kite
    context_object_name = 'kite_list'
    template_name = 'myapp/kitelist.html'


class KiteDetailView(DetailView):
    model = Kite
    context_object_name = 'kite_detail'
    template_name = 'myapp/kitedetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class KiteCreateView(CreateView):
    fields = '__all__'
    model = Kite
    template_name = 'myapp/addkite.html'


class KiteUpdateView(UpdateView):
    model = Kite
    fields = '__all__'
    template_name = 'myapp/updatekite.html'


class KiteDeleteView(DeleteView):
    model = Kite
    context_object_name = 'kite'
    success_url = reverse_lazy('myapp:list')
    template_name = 'myapp/deletekite.html'
