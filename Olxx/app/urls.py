from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home),
    path('reg/',views.registration),
    path('regdata/',views.registrationdata),
    path('otp/',views.Fotp),
    path('verifyotp/',views.verifyotp),
    path('loginp/',views.login),
    path('log-in-data/',views.logincredentials),
]
