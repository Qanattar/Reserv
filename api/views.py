from django.shortcuts import render, redirect

from api.forms import RecordForm, ClientForm
from api.models import *
from django.forms import modelform_factory, inlineformset_factory
from django.core.mail import send_mail


# Create your views here.
def main(request):
    return render(request, 'main.html')


def hello_page(request):
    return render(request, 'hello_page.html')


def clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})


def client_detail(request, pk):
    client = Client.objects.get(id=pk)
    records = client.records_set.all()
    content = {'client': client, 'records': records}
    return render(request, 'client_detail.html', content)


def times(request):
    dates = Time.objects.all()
    return render(request, 'dates.html', {'dates': dates})


def registration_page(request):
    ClientFormSet = modelform_factory(Client, fields=('name', 'email', 'phone_number'))
    formset = ClientFormSet()
    if request.method == 'POST':
        formset = ClientFormSet(request.POST)
        if formset.is_valid():
            formset.save()
        client_id = Client.objects.last()
        return redirect('client_detail',  client_id.id)
    return render(request, 'registration.html', {'formset': formset})


def create_record(request, pk):
    client = Client.objects.get(id=pk)
    RecordFormSet = inlineformset_factory(Client, Records, fields=('client', 'time'))
    formset = RecordFormSet(queryset=Records.objects.none(), instance=client)
    if request.method == 'POST':
        formset = RecordFormSet(request.POST, instance=client)
        if formset.is_valid():
            formset.save()
            return redirect('client_detail', pk)
    send_email(request, pk)
    return render(request, 'create_record.html', {'formset': formset})


def delete_record(request, pk):
    record = Records.objects.get(id=pk)
    if request.method == "POST":
        record.delete()
        return redirect('client_detail', record.client.id)

    return render(request, 'delete_record.html', {'record': record})


def update_record(request, pk):
    record = Records.objects.get(id=pk)
    form = RecordForm(instance=record)

    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('client_detail', record.client.id)

    context = {'form': form}
    return render(request, 'update_record.html', context)


def send_email(request, pk):
    client = Client.objects.get(id= pk)
    send_mail('You have successfully recorded', 'Hello, You have successfully recorded ', 'kanat_1406@mail.ru',
              [client.email], fail_silently=False)
    return render(request, 'send_email.html')
