from django.shortcuts import render
from django.views.generic import ListView
from .models import Parser

class InputView(ListView):
    model = Parser
    template_name = 'parser_list.html'
    context_object_name = 'input'





# Create your views here.
