from django.shortcuts import render
from DjangoModel1.models import Employee

# Create your views here.
def employeeData(request):
    empleados = Employee.objects.all()
    data = {'empleados':empleados}
    return render(request, 'DjangoModel1/empleados.html', data)