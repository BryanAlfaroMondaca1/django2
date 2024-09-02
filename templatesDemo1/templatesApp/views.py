from django.shortcuts import render

# Create your views here.
def renderizar(request):
    return render(request,"templatesApp/pagina1.html")

def renderizar(request):
    data = {"nombre" : "Paul"}
    return render(request,'templatesApp/pagina2.html', data)