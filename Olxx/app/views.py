from django.shortcuts import render
from .models import User
import math,random
from django.core.mail import send_mail
from datetime import timezone,timedelta,datetime
from django.contrib.auth.hashers import make_password,check_password
from django.conf import settings
# Create your views here.


def Home(request):
    return render(request,'home.html')

def registration(request):
    return render(request,'registration.html')

def registrationdata(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        gender=request.POST['gender']
        state=request.POST['state']
        zipcode=request.POST['zipcode']
        address=request.POST['address']
        password=request.POST['password']

        if User.objects.filter(email=email).exists():
            return render(request,'registration.html',{'msg':'email already registered'})
        else:
            
            otp=get_otp()

            data=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,gender=gender,state=state,zipcode=zipcode,address=address,
            password=make_password(password),otp=otp)

            email=data.email
            subject="OTP for Verification"
            message=f"One-Time-Password is : {otp} Valid for 3 min only & usable only once on Verification T&C apply."
            email_from=settings.EMAIL_HOST_USER
            to=email
            recipient_list = [to,]
            send_mail( subject, message, email_from, recipient_list )
            return render(request,'otp.html',{'msg':'Check your Email and Verify your Id Using OTP'})


def get_otp():
    digits="0123456789"
    OTP=""
    for i in range(5):
        OTP+=digits[math.floor(random.random()*10)]
    return OTP


def Fotp(request):
    return render(request,'otp.html')

def verifyotp(request):
    if request.method=='POST':
        otp=request.POST['otp']
        email=request.POST['email']
        if User.objects.filter(email=email,otp=otp):
            user=User.objects.get(email=email)
            user.is_verified=True
            user.save()
            return render(request,'home.html',{'user':user})
        return render(request,'check.html')

def login(request):
    return render(request,'login.html')

def logincredentials(request):
        if request.method=='POST':
            email=request.POST['email']
            password=request.POST['password']

            if User.objects.filter(email=email).exists():
                user=User.objects.get(email=email)
                dbpassword=user.password
                if check_password(dbpassword,password):
                    if user.is_verified==True:
                        return render(request,'home.html',{'user':user})
                    else:
                        return render(request,'login.html',{'msg':'user is not verified plzz verifiy your email'})
                else:
                    return render(request,'login.html',{'msg':'password was incorrect plzz enter valid password'})
            else:
                return render(request,'login.html',{'msg':'email does not exists'})