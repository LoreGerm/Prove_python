from django.shortcuts import render
from .forms import FormMsg
from django.contrib import messages

# Create your views here.
def form(request):

    if request.method == 'POST':
        form = FormMsg(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Il messaggio è stato inviato')
        else:
            messages.success(request, 'Errore')

    return render(request, 'Form/form.html')