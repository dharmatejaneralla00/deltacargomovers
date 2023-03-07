from django.db import models

# Create your models here.

class Booking(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=6)
    fromadd = models.CharField(max_length=100)
    toadd = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    toname = models.CharField(max_length=100)
    fno = models.IntegerField()
    tono = models.IntegerField()
    pcs = models.IntegerField()
    wt = models.DecimalField(max_digits=5,decimal_places=3)
    invoiceno = models.IntegerField()
    invoiceamt = models.DecimalField(max_digits=5,decimal_places=3)
    charges = models.DecimalField(max_digits=5,decimal_places=3)
    freightcharges = models.DecimalField(max_digits=5,decimal_places=3)
    lrcharges = models.DecimalField(max_digits=5,decimal_places=3)
    door_delivery_charges = models.DecimalField(max_digits=5,decimal_places=3)
    others_charges = models.DecimalField(max_digits=5,decimal_places=3)
    total_charges = models.DecimalField(max_digits=5,decimal_places=3)
    uid = models.CharField(max_length=20,primary_key=True)

    def __str__(self):
        return self.uid