from django.shortcuts import render
from base.forms import ContatoForm

def inicio(request):
  return render(request, 'inicio.html')

def contato(request):
  sucesso = False
  form = ContatoForm(request.POST or None)
  if form.is_valid():
      sucesso = True
      form.save()
  contexto = {
    'telefone': '(99) 9999-9999',
    'responsavel': 'Zé linguiça',
    'form': form,
    'sucesso': sucesso
  }
  return render(request, 'contato.html', contexto)