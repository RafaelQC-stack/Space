from django.shortcuts import render


def index(request):

    dados = { 

    1:{"nome":"Nebulosa de Carina",
       "legenda":"webbtelescope.org / NASA / James Webb"},
    2:{"nome": "Galáxia NGC 1079",
       "legenda": "nasa.org / NASA / Hubble"},
    3:{"nome": "Galáxia de Andromeda",
       "legenda":"nasa.vnn / NASA / Hubble"}
             }
    
    return render(request,'index.html', {"cards": dados})

def imagem(request):
    return render(request, 'imagem.html')
