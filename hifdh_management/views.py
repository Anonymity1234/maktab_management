from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from hifdh_management.models import Hifdh_Table

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import AccessMixin

class HifdhTableView(TemplateView):
    model = Hifdh_Table
    template_name = 'index.html'
    # login_url = 'login'
    # redirect_field_name = 'redirect_to'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['request'] = self.request
        return context

    def post(self, request):
        print(request.POST)
        form = request.POST
        print(form)
        return render(request, 'index.html', {})