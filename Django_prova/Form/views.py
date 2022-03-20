from django.shortcuts import render, redirect
from Form.models import utente
from .forms import FormMsg
from django.contrib import messages


def form(request):
    if request.method == 'POST':
        form = FormMsg(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Il messaggio è stato inviato')
        else:
            messages.success(request, 'Errore')

    return render(request, 'Form/form.html')


def messaggi(request):
    mess = utente.objects.all()
    context = {'mess':mess}
    return render(request, 'Form/mess.html', context)


def elimina(request, id):
    ut = utente.objects.get(id = id)
    ut.delete()
    return redirect('mess')