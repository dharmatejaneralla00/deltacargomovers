from django.db import models

# Create your models here.

class Booking(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=6)
    fromadd = models.CharField(max_length=100)
    toadd = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    toname = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    fno = models.IntegerField()
    tono = models.IntegerField()
    pcs = models.IntegerField()
    wt =  models.IntegerField()
    invoiceno = models.IntegerField()
    invoiceamt =  models.IntegerField()
    charges =  models.IntegerField()
    freightcharges =  models.IntegerField()
    lrcharges =  models.IntegerField()
    door_delivery_charges =  models.IntegerField()
    others_charges =  models.IntegerField()
    total_charges =  models.IntegerField()
    lrno = models.CharField(max_length=20,primary_key=True)
    bookedarea= models.CharField(max_length=10)
    bookeduser = models.CharField(max_length=10)
    desc = models.CharField(max_length=10)
    ewaybillno = models.CharField(max_length=10)
    def __str__(self):
        return self.lrno