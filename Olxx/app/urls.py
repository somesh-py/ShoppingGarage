from django.urls import path
from . import views


urlpatterns = [
    path('home/',views.Home),
    path('',views.registration),
    path('regdata/',views.registrationdata),
    path('otphtml/',views.otphtml),
    path('verify-otp/',views.verifyotp),
    path('loginp/',views.login),
    path('log-in-data/',views.logincredentials),
]
