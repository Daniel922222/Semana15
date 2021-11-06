from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from.models import datos
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    Datosl=datos.objects.all()
    return render(request,"uno.html",{"datos":Datosl})
    
def registrardatos(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    apellido=request.POST['txtapellido']


    dato=datos.objects.create(codigo=codigo,nombre=nombre,apellido=apellido)
    return redirect('/')




def eliminardatos(request,codigo):
    dato=datos.objects.get(codigo=codigo)
    dato.delete()
    return redirect('/')


def autor(rquest):
     return HttpResponse("Oscar Daniel benitez blanco")
