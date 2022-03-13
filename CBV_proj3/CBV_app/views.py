from django.shortcuts import render
from .models import Company
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView


# Create your views here.


class Company_list_view(ListView):
    model = Company
    context_object_name = 'companies'
    template_name = 'CBV_app/company_list.html'


class Company_Details_view(DetailView):
    model = Company
    context_object_name = 'companies'
    template_name = 'CBV_app/company_info.html'


class Company_create_view(CreateView):
    model = Company
    fields = ['name', 'location', 'ceo']
    template_name = 'CBV_app/company_create.html'


class Company_update_view(UpdateView):
    model = Company
    fields = ['name', 'ceo']
    context_object_name = 'companies'
    template_name = 'CBV_app/company_create.html'


class Company_delete_view(DeleteView):
    model = Company
    context_object_name = 'companies'
    success_url = reverse_lazy('CBV_app:home')
    template_name = 'CBV_app/company_conform_delete.html'

