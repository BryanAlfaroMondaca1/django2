from django.shortcuts import render




def renderizar5(request):
    data = {"nombre" : "Paul","ID":123}
    return render(request,'templatesApp/userInfoTemplate.html', data)
