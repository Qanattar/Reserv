from django.forms import ModelForm
from .models import Records, Client


class RecordForm(ModelForm):
    class Meta:
        model = Records
        fields = ['time']


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['id', 'name', 'phone_number', 'email']
