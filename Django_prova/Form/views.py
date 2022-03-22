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

    context = {
        'nome': '',
        'cognome': '',
        'email': '',
        'views': 'form',
        'msc': 'Mandami un messaggio',
        'btn': 'Invia'
    }
    return render(request, 'Form/form.html', context)


def messaggi(request):
    ut = utente.objects.all()
    context = {'utenti':ut}
    return render(request, 'Form/mess.html', context)


def elimina(request, id):
    ut = utente.objects.get(id = id)
    ut.delete()
    


def update(request, id):
    ut = utente.objects.get(id = id)
    if request.method == 'POST':
        form = FormMsg(request.POST, instance=ut)
        if form.is_valid:
            form.save()
            return redirect('mess')
        else:
            messages.success(request, 'Errore')

    context = {
        'nome': ut.nome,
        'cognome': ut.cognome,
        'email': ut.email,
        'messaggio': ut.messaggio,
        'utente': id,
        'views': 'update',
        'msc': 'Modifica messaggio',
        'btn': 'Conferma'
    }
    return render(request, 'Form/form.html', context)


def cerca(request):
    if request.method == 'POST':
        cerca = request.POST['cerca']
        ut = utente.objects.filter(nome__icontains=cerca)

        context = {
            'utenti': ut,
        }
    return render(request, 'Form/cerca.html', context)