from django.urls import path
from .import views

urlpatterns = [

    path('', views.arquivoList, name='arquivo-list'),
    path('arquivo/<int:id>', views.arquivoView, name='arquivo-view'), # url's (rota) e nome da view
    path('newarquivo/', views.newArquivo, name="new-arquivo"),
    path('edit/<int:id>', views.editArquivo, name="edit-arquivo"),
    path('delete/<int:id>', views.deleteArquivo, name="delete-arquivo"),
    path('sobre/', views.sobre),
    path('biometria/', views.biometria),
    path('biom_digital/', views.biom_digital)

]
