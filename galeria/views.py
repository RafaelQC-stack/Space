from django.shortcuts import render, get_object_or_404

from galeria.models import Fotografia


def index(request):
    fotografias = Fotografia.objects.filter(publicada=True)
    
    return render(request,'index.html', {"cards":fotografias })

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'imagem.html', {"fotografias": fotografia})

def buscar(request):
    return render (request, "buscar.html")
