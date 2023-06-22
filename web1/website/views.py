from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests,"index.html")

def contato(requests):
    return render(requests,"contato.html")

def sobre(requests):
    return render(requests,"sobre.html")

def projetos(requests):
    return render(requests,"projetos.html")