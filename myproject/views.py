from django.shortcuts import render
from .models import Persona
from .forms import PersonaForm

def registro_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_persona')
    else:
        form = PersonaForm()
    personas = Persona.objects.all()
    return render(request, 'registro_persona.html', {'form': form, 'personas': personas})
