from django.apps import apps
from django.shortcuts import render, redirect
from . import models

# Create your views here.
clientlists = apps.get_model('login','clientlist')
destinations = apps.get_model('login','Destination')
userlogin = apps.get_model('login','userLogins')
def uidgenerate(r):
    details = userlogin.objects.get(username = r.user.username)
    area = details.areacode
    lrno = details.lrno
    print(lrno)
    lrno = str(int(lrno.replace(area,""))+1).rjust(4,'0')
    newlrno = str(area)+lrno
    print(newlrno)
    return newlrno
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
            totalcharges = r.POST.get('totalcharge',False)
            door_delivery_charge = r.POST['door_delivery_charge']
            # fname = r.POST['fromname']
            fname= r.POST.get('fromname',False)
            tname = r.POST['tname']
            # fadd = r.POST['fadd']
            fadd = r.POST.get('fadd',False)
            tadd = r.POST['tadd']
            # fno = r.POST['fno']
            fno = r.POST.get('fno',False)
            tno = r.POST['tno']
            desc = r.POST['desc']
            if r.POST['paid'] == 'paid':
                paid = True
            else:
                paid = False
            userdetails = userlogin.objects.get(username=r.user.username)
            lrno = uidgenerate(r)
            models.Booking(date, ctype, fadd, tadd, fname, tname,destination, paid,fno, tno, pcs, wt, invno, invamt, charges, frcharges,
                           lrcharges, door_delivery_charge, othercharges, totalcharges, lrno,userdetails.area,userdetails.username,desce).save()
            userdetails.lrno = lrno
            userdetails.save()
            return redirect('dashboard/')
    else:
        return redirect('login/')
