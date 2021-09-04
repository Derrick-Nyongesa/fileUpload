from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CsvForm
from django.conf import settings
import os
import csv
from .models import Invoice, InvoiceUpload
from datetime import datetime


# Create your views here.
def save_csv(file_path):
    records = []
    with open(file_path, 'r', newline='', encoding='ISO-8859-1') as fp:
        invoices = csv.reader(fp, delimiter=',')
        row = 0
        for invoice in invoices:
            if row==0:
                row = row + 1
            else:
                # create a dictionary of invoice details
                records.append(Invoice(
                    invoice_no = invoice[0],
                    stock_code = invoice[1],
                    description = invoice[2],
                    quantity = int(invoice[3]),
                    invoice_date = datetime.strptime(invoice[4], "%m/%d/%Y %H:%M"),
                    unit_price = float(invoice[5]),
                    customer_id = invoice[6],
                    country = invoice[7],
                ))
                

                row = row + 1
        fp.close()
    Invoice.objects.bulk_create(records)


def upload(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CsvForm(data=request.POST, files=request.FILES)
        # check whether it's valid:
        if form.is_valid():
            csvfile = form.save()
            file_path = csvfile.file.path
            print(file_path)
            save_csv(file_path)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('success')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CsvForm()

    return render(request, 'upload.html', {'form': form})

def success(request):
    
    return render(request, 'success.html')

def uploaded_file(request):
    invoice = Invoice.objects.all()
    return render(request, 'uploadedFile.html', {'invoice':invoice})


