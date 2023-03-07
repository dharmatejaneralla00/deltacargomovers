from django.apps import apps
from django.shortcuts import render, redirect
from . import models

# Create your views here.
clientlists = apps.get_model('login','clientlist')
def view_booking(r):
    if r.user.is_authenticated:
        return render(r,'Booking.html',{'clientlist':clientlists.objects.all()})
    else:
        return redirect('login/')


def book(r):
    if r.user.is_authenticated:
        if r.method ==  'POST':
            date = r.POST['date']
            ctype = r.POST['cashcredit']
            clientlist = r.POST['clientlist']
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
            if ctype == 'cash':
                fname = r.POST['fname']
                tname = r.POST['tname']
                fadd = r.POST['fadd']
                tadd = r.POST['tadd']
                fno = r.POST['fno']
                tno = r.POST['tno']
            else:
                c = clientlists.objects.get(clientname = clientlist)
                fname = c.fname
                tname = c.toname
                fadd = c.fromadd
                tadd = c.toadd
                fno = c.fno
                tno = c.tono
            models.Booking(date, ctype, fadd, tadd, fname, tname, fno, tno, pcs, wt, invno, invamt, charges, frcharges,
                           lrcharges, door_delivery_charge, othercharges, totalcharges, 1).save()
            return redirect('dashboard/')
    else:
        return redirect('login/')
