"""
URL configuration for sem6 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tour_and_travalling.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', index,name="index"),
    path('profile_management/', profile_management,name="profile_management"),
    path('profile/', profile,name="profile"),
    path('payment_history/', payment_history,name="payment_history"),
    path('search/', search,name="search"),
    path('offers/', offers,name="offers"),
    path('login/', loginuser,name="login"),
    path('register/', register,name="register"),
    path('booking/', bookingtour,name="booking"),
    path('payment/', payment_tour,name="payment"), 
    path('bookingconformation/', bookingcon,name="bookingconformation"),
    path('place_info/', place_info,name="place_info"), 
    path('superadmin/', superadmin,name="superadmin"), 
    path('Review/',Review ,name="Review"),
    path('manageuser/',manageuser ,name="manageuser"),
    path('managehotel/',managehotel ,name="managehotel"),
    path('managepackeg/',managepackeg ,name="managepackeg"),
    path('managefeedback/',managefeedback ,name="managefeedback"),
    path('managepayment/',managepayment ,name="managepayment"),
    path('managerating/',managerating ,name="managerating"),
    path('upi/',upi ,name="upi"),
    path('tourcondition/',tourcondition,name="tourcondition"),
    path('logout_user/',logout_user,name="logout_user"),
    path('managedelete/',managedelete,name="managedelete"),
    path('editpackeg/',editpackeg,name="editpackeg"),
    path('edithotel/',edithotel,name="edithotel"),
    path('showuserdata/',showuserdata,name="showuserdata"),
    path('addpack/',addpack,name="addpack"),
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
