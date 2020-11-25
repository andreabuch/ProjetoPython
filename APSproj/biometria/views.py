from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse

#from .forms import ArquivoForm
from django.contrib import messages

def biometria(request):
    return render(request, 'arquivos/biometria.html')