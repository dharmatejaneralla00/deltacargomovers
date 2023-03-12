import os.path
from wsgiref.util import FileWrapper

from django.http import HttpResponse, StreamingHttpResponse
from docxtpl import DocxTemplate
from django.apps import apps
from django.shortcuts import render, redirect
from . import models
import  docx2pdf
from pathlib import Path
import mimetypes

BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.
clientlists = apps.get_model('login','clientlist')
destinations = apps.get_model('login','Destination')
userlogin = apps.get_model('login','userLogins')
def uidgenerate(r):
    details = userlogin.objects.get(username = r.user.username)
    area = details.areacode
    lrno = details.lrno
    lrno = str(int(lrno.replace(area,""))+1).rjust(4,'0')
    newlrno = str(area)+lrno
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
            fname= r.POST.get('fromname',False)
            tname = r.POST['tname']
            fadd = r.POST.get('fadd',False)
            tadd = r.POST['tadd']
            fno = r.POST.get('fno',False)
            tno = r.POST['tno']
            desc = r.POST['desc']
            ewaybillno = r.POST['ewaybillno']
            if r.POST['paid'] == 'paid':
                paid = True
            else:
                paid = False
            userdetails = userlogin.objects.get(username=r.user.username)
            lrno = uidgenerate(r)
            models.Booking(date, ctype, fadd, tadd, fname, tname,destination, paid,fno, tno, pcs, wt, invno, invamt, charges, frcharges,
                           lrcharges, door_delivery_charge, othercharges, totalcharges, lrno,userdetails.area,userdetails.username,desc,ewaybillno).save()
            userdetails.lrno = lrno
            userdetails.save()
            generatetemplate(date,fadd,tadd,fno,tno,fname,tname,destination,paid,pcs,wt,invno,invamt,charges,frcharges,lrcharges,door_delivery_charge,othercharges,totalcharges,lrno,desc,ewaybillno,userdetails.officeadd)
            # return redirect('bookedlrdownload/'+lrno)
            # return redirect('booking/')
            filepath = os.path.join(BASE_DIR, 'templates/bookedlr/pdf/' + lrno + '.pdf')
            res = HttpResponse(open(filepath, 'rb').read(), content_type='application/pdf')
            res['Content-Disposition'] = 'attachment;filename=' + os.path.basename(filepath)
            return res
        return  redirect('booking/')
    else:
        return redirect('login/')

def generatetemplate(date,fadd,tadd,fno,tno,fname,tname,destination,paid,pcs,wt,invno,invamt,charges,frch,lrch,ddch,other,total,lrno,desc,ewaybill,branchadd):
    # doc = DocxTemplate('bookingtemplate.docx')
    doc = DocxTemplate(os.path.join(BASE_DIR,'templates/bookingtemplate.docx'))
    if paid:
        ptype = 'PAID'
    else:
        ptype = 'TO PAY'
    context = {
        "fromname":fname,"fromadd":fadd,"fromno":fno,'toname':tname,'toad':tadd,'tono':tno,'desc':desc,
        'pcs':pcs,'wt':wt,'invno':invno,'invamt':invamt,'destination':destination,'lrno':lrno,'paytype':ptype,
        'char':charges,'frch':frch,'lrch':lrch,'ddch':ddch,'other':other,'total':total,'branchadd':branchadd,"date":date,'ewaybillno':ewaybill
    }
    doc.render(context)
    filename = "templates/bookedlr/doc/"+lrno+".docx"
    doc.save(os.path.join(BASE_DIR,filename))
    # pythoncom.CoInitialize()
    docx2pdf.convert(os.path.join(BASE_DIR,filename),os.path.join(BASE_DIR,'templates/bookedlr/pdf/',lrno+".pdf"))

def bookedlrdownload(r,name):
    filepath = os.path.join(BASE_DIR,'templates/bookedlr/pdf/'+name+'.pdf')
    res = HttpResponse(open(filepath,'rb').read(),content_type='application/pdf')
    res['Content-Disposition'] = 'attachment;filename='+os.path.basename(filepath)
    return res