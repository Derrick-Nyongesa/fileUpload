from django import forms
from django.db.models import fields
from .models import InvoiceUpload

class CsvForm(forms.ModelForm):
    class Meta:
        model = InvoiceUpload
        fields = ('file',)