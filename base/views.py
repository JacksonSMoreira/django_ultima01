from django.shortcuts import render
#from django.http import HttpResponse
from base.forms import ContatoForm

# Create your views here.
def inicio(request):
    return render(request,'inicio.html')

def contato(request):
    sucesso = False
    if request.method == 'GET':
       form = ContatoForm()
    else:
       form = ContatoForm(request.POST)
       if form.is_valid():
           sucesso = True
    contexto = {
        'telefone': '(99) 99999.99999',
        'responsavel': ' Maria da Silva Pereira',
        'form': form,
        'sucesso': sucesso
    }
    return render(request,'contato.html', contexto)
'''if request.method == 'POST':
        print(request.POST)'''
    