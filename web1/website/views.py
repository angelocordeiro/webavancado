from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests,"index.html")

def w3c(requests):
    return render(requests,"w3c.html")

def html(requests):
    return render(requests,"html.html")