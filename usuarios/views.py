from django.shortcuts import render


from usuarios.forms import loginForms, CadastroForms


def login(request):
    form = loginForms()
    return render(request, "login.html", {"form": form})



def cadastro(request):
    form = CadastroForms(

    )
    return render(request, "cadastro.html", {"form":form})