from django.shortcuts import render

# Create your views here.
def lista_empleados(request):
    empleados = ['Vanessa Morales','Brian Diaz','Natalia Peña', 'Nicole Pinilla' , 'Valery Maragaño']
    return render(request, 'app_empleados/lista_empleados.html',{'empleados': empleados})