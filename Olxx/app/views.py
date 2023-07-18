from django.shortcuts import render,redirect
from .models import User
import math,random
from django.core.mail import send_mail
from datetime import timezone,timedelta,datetime
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
# Create your views here.


def Home(request):
    return render(request,'home.html')

def registration(request):
    return render(request,'registration.html')


def registrationdata(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        state = request.POST.get('state')
        zipcode = request.POST.get('zipcode')
        address = request.POST.get('address')
        password = request.POST.get('password')
        password_hash = make_password(password)

        if User.objects.filter(email=email).exists():
            return render(request, 'registration.html', {'msg': 'Email already registered.'})
        else:
            otp = get_otp()

            user = User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                email=email,
                gender=gender,
                state=state,
                zipcode=zipcode,
                address=address,
                password=password,
                otp=otp
            )

            subject = "OTP for Verification"
            message = f"One-Time Password is: {otp}. It is valid for 3 minutes only and can be used only once for verification. Terms and conditions apply."
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, email_from, recipient_list)

            return render(request, 'otp.html')

    else:
        return render(request, 'registration.html')

def get_otp():
    digits="0123456789"
    OTP=""
    for i in range(5):
        OTP+=digits[math.floor(random.random()*10)]
    return OTP


def otphtml(request):
    return render(request,'otp.html')


def verifyotp(request):
    if request.method=='POST':
        email=request.POST['email']
        otp=request.POST['otp']
        if User.objects.filter(email=email,otp=otp).exists():
            user=User.objects.get(email=email)
            user.is_verified=True
            user.save()
            return render(request,'login.html')
        else:
            return render(request,'otp.html',{'msg':'enter correct informations'})

def login(request):
    return render(request,'login.html')

def logincredentials(request):
        if request.method=='POST':
            email=request.POST['eemail']
            ppassword=request.POST['ppassword']

            if User.objects.filter(email=email).exists():
                user=User.objects.get(email=email)
                print(user)
                password=user.password
                print(password)
                # if check_password(ppassword,dbpassword):
                if User.objects.filter(password=password).exists():
                    if user.is_verified==True:
                        user=User.objects.get(email=email)
                        print(user)
                        return render(request,'home.html',{'user':user})
                    else:
                        return render(request,'login.html',{'msg':'user is not verified plzz verifiy your email'})
                else:
                    return render(request,'login.html',{'msg':'password was incorrect plzz enter valid password'})
            else:
                return render(request,'login.html',{'msg':'email does not exists'})


# def logincredentials(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         if User.objects.filter(email=email).exists():
#             user = User.objects.get(email=email)
#             dbpassword = user.password

#             if check_password(password, dbpassword):
#                 if user.is_verified:
#                     return render(request, 'home.html', {'user': user})
#                 else:
#                     return render(request, 'login.html', {'msg': 'User is not verified. Please verify your email.'})
#             else:
#                 return render(request, 'login.html', {'msg': 'Incorrect password. Please enter a valid password.'})
#         else:
#             return render(request, 'login.html', {'msg': 'Email does not exist.'})
#     else:
#         return render(request, 'login.html')


# def logincredentials(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         user = authenticate(request, email=email, password=password)

#         if user is not None:
#             if user.is_verified:
#                 return render(request, 'home.html', {'user': user})
#             else:
#                 return render(request, 'login.html', {'msg': 'User is not verified. Please verify your email.'})
#         else:
#             return render(request, 'login.html', {'msg': 'Incorrect email or password.'})

#     else:
#         return render(request, 'login.html')


# def logincredentials(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         if User.objects.filter(email=email).exists():
#             user = User.objects.get(email=email)

#             if user.check_password(password):
#                 if user.is_verified:
#                     return render(request, 'home.html', {'user': user})
#                 else:
#                     return render(request, 'login.html', {'msg': 'User is not verified. Please verify your email.'})
#             else:
#                 return render(request, 'login.html', {'msg': 'Incorrect password. Please enter a valid password.'})
#         else:
#             return render(request, 'login.html', {'msg': 'Email does not exist.'})
#     else:
#         return render(request, 'login.html')