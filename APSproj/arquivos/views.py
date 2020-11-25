from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from .forms import ArquivoForm
from django.contrib import messages
from .models import Arquivo
#from matplotlib import pyplot as plt
#import cv2

@login_required
def arquivoList(request):  #resgata dados do banco

    search = request.GET.get('search') # search = name input da busca
    if search:
        arquivo = Arquivo.objects.filter(title__icontains=search)
    else:
        arquivos_list = Arquivo.objects.all().order_by('-created_at') #ordem de criação
        paginator = Paginator(arquivos_list, 4)  # particionado para visualização 4 arquivos
        page =request.GET.get('page')  # resgata total de paginas para quantidade existente arquivo
        arquivos = paginator.get_page(page)  # pagina atual e numero maximo
        return render(request,'arquivos/list.html',{'arquivos':arquivos}) #retorna o template desejado

@login_required
def arquivoView(request,id): # retorna os dados do banco ou retorna erro
    arquivo = get_object_or_404(Arquivo, pk=id) # pega somente um objeto do banco e envia
    return render(request, 'arquivos/arquivo.html', {'arquivo': arquivo}) # envia dados para template

@login_required
def newArquivo(request):
    if request.method == 'POST':
        form = ArquivoForm(request.POST)

        if form.is_valid():
            arquivo = form.save(commit=False)
            arquivo.categoria = 'rest' #por padrão será restrito
            arquivo.user = request.user
            arquivo.save()
            return redirect('/') # retorna tela
    else:
        form = ArquivoForm()
        return render(request, 'arquivos/addarquivo.html', {'form':form}) #template arquivos/...



@login_required
def editArquivo(request, id):
    arquivo = get_object_or_404(Arquivo,pk=id)
    form = ArquivoForm(instance=arquivo)

    if(request.method == 'POST'):
        form = ArquivoForm(request.POST, instance=arquivo)

        if(form.is_valid()):
            arquivo.save()
            messages.info(request, "Arquivo alterado com sucesso!")
            return redirect('/')
        else:
            return render(request, 'arquivos/editarquivo.html', {'form': form, 'arquivo': arquivo})

    else:
        return render(request, 'arquivos/editarquivo.html', {'form':form, 'arquivo':arquivo})


@login_required
def deleteArquivo(request, id):
    arquivo = get_object_or_404(Arquivo, pk=id)
    arquivo.delete()
    messages.info(request, "Arquivo excluido com sucesso!")
    return redirect('/')


def sobre(request):
    return render(request, 'arquivos/sobre.html')
    return HttpResponse('Seja bem vindo')


def biometria(request):
    return render(request, 'arquivos/biometria.html')


def biom_digital(request):
    return render(request, 'arquivos/biom_digital.html') #atualizar conforme img processada
   

def process_img():
    pass


