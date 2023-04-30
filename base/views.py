from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def contato(request):
    contexto = {
        'telefone': '(99) 99999.99999',
        'responsavel': ' Maria da Silva Pereira'
    }
    return render(request,'contato.html', contexto)