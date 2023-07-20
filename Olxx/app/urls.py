from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.Home),
    path('reg/',views.registration),
    path('regdata/',views.registrationdata),
    path('otphtml/',views.otphtml),
    path('verify-otp/',views.verifyotp),
    path('loginp/',views.login),
    path('log-in-data/',views.logincredentials),
    path('product-placed/',views.productpalced),
    path('product-placed-data/',views.productpalceddata),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
