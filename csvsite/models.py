from django.db import models

# Create your models here.
class Invoice(models.Model):
    invoice_no = models.CharField(max_length=10, blank=True, null=True)
    stock_code = models.CharField(max_length=10, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    quantity = models.IntegerField()
    invoice_date = models.DateTimeField()
    unit_price = models.FloatField()
    customer_id = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)

    @classmethod
    def all_invoices(cls):
        return cls.objects.all()


class InvoiceUpload(models.Model):
  file = models.FileField(upload_to='invoices/')

