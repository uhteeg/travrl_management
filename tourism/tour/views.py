from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import *
from django.contrib import messages
import logging


# Create your views here.
logger = logging.getLogger(__name__)
def index(req):
    return render(req,"index.html")

def home(req):
    return render(req,"home.html")
def about(req):
    return render(req,"about.html")
def gallery(req):
    return render(req,"gallery.html")
def contact(req):
    return render(req,"contact.html")
def service(req):
    return render(req,"service.html")
def single(req):
    return render(req,"single.html")
def login(req):
    logger.info("View accessed with user %s", req.method)
    if req.method == 'POST':
        u=req.POST['uname']
        p=req.POST['pswd']
        logger.info("View accessed with user %s %s", u,p)
        try:
            data1=reguser.objects.get(name=u)
            if data1.password == p:
                logger.info("success")
                req.session['id'] = u
                messages.success(req,'login successfully')
                logger.info(data1)
                context = {'user': data1}
                return render(req,'index.html',context)
            else:
                logger.info("incorrect password")
                messages.error(req,'incorrect password')
                return  render(req,'index.html',{'user',data1})
        except Exception as e:
            logger.exception("An error occurred: %s", e)
            if u == 'admins' and p == 'admins':
                req.session['id1']=u
                return  render(req,'index.html')
    else:
        return render(req,'login.html')
def register(req):
    if req.method == 'POST':
        username=req.POST['uname']
        password=req.POST['pswd']
        email=req.POST['email']
        phone=req.POST['phone']
        address=req.POST['address']
        data=reguser.objects.create(name=username,password=password,email=email,phone=phone,address=address)
        data.save()
        return redirect(index)
    else:
        return render(req,'registration.html')
# Create your views here.
def driver(req):
    return render(req,'driver.html')
def hotel(req):
    return render(req,'hotel.html')
def tourpackages(req):
    return render(req,'tourpackages.html')
def home(req):
    return  render(req,'home.html')