# Create your views here.

from django.shortcuts import render, redirect
from apps.medicamento.form import MedicamentoForm
  
def index(request):  
    med = MedicamentoForm()  
    return render(request,"index.html",{'form':med})

def add(request):
    # Creamos un formulario vacío
    form = MedicamentoForm()

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = MedicamentoForm(request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manejarla
            instancia = form.save(commit=False)
            # Podemos guardarla cuando queramos
            instancia.save()
            # Después de guardar redireccionamos a la lista
            return redirect('/admin')

    # Si llegamos al final renderizamos el formulario
    return render(request, "add.html", {'form': form})