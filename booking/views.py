from django.apps import apps
from django.shortcuts import render, redirect
from . import models

# Create your views here.
clientlists = apps.get_model('login','clientlist')
destinations = apps.get_model('login','Destination')
def view_booking(r):
    if r.user.is_authenticated:
        return render(r,'Booking.html',{'clientlist':clientlists.objects.all(),'destinations':destinations.objects.all()})
    else:
        return redirect('login/')


def book(r):
    if r.user.is_authenticated:
        if r.method ==  'POST':
            date = r.POST['date']
            ctype = r.POST['cashcredit']
            destination = r.POST['destination']
            pcs = r.POST['pcs']
            wt = r.POST['wt']
            invamt = r.POST['invamt']
            invno = r.POST['invno']
            charges = r.POST['charge']
            lrcharges = r.POST['lrcharge']
            frcharges = r.POST['frcharge']
            othercharges = r.POST['othercharge']
            totalcharges = r.POST['totalcharge']
            door_delivery_charge = r.POST['door_delivery_charge']
            fname = r.POST['fname']
            tname = r.POST['tname']
            fadd = r.POST['fadd']
            tadd = r.POST['tadd']
            fno = r.POST['fno']
            tno = r.POST['tno']
            models.Booking(date, ctype, fadd, tadd, fname, tname,destination, fno, tno, pcs, wt, invno, invamt, charges, frcharges,
                           lrcharges, door_delivery_charge, othercharges, totalcharges, 1).save()
            return redirect('dashboard/')
    else:
        return redirect('login/')
