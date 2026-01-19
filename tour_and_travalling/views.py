from datetime import date
import os
from django.shortcuts import get_object_or_404, render,redirect
from django.http import FileResponse, HttpResponse
from tour_and_travalling import models
from tour_and_travalling.models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
import uuid
from django.core.files.storage import FileSystemStorage

import re




def index(request):
    
    if request.method=="POST":
     pack=package.objects.all()
     search=request.POST.get('search')
     return render(request,'travel/home/index.html',{'pack':pack,'search':search})
    
    pack=package.objects.all()
    return render(request,"travel/home/index.html",{'pack':pack} )
    

def admin_home(request):
 return render(request,"travel/admin_home.html")

def search(request):
    
    return render(request,"travel/home/search.html")

def offers(request):
    pack=package.objects.all()
    return render(request,"travel/home/offers.html",{'pack':pack})


def loginuser(request):  
      if request.method=='POST':
          name=request.POST.get('name')
          password=request.POST.get('pass')
          user=authenticate(username=name,password=password)
          if user is not None:
           login(request,user)
           return redirect('index')
          
          elif name=='parth_ramanujj' and password=='parth':
            
            return redirect('superadmin')
          else:
            return redirect('login')
        #   else:
        #       return render(request,"home/index.html")
      context={
          'login1':user_login.objects.all()
      }      
      return render(request,"travel/home/login.html",context)
       
def logout_user(request):
        logout(request)
        return  redirect('index')

def register(request):
    
    if request.method=='POST':
          name=request.POST.get('name')
          email=request.POST.get('email')
          password=request.POST.get('pass')
          conpassword=request.POST.get('cpass')
          image=request.POST.get('image')
          reg=ragister(name=name,email_id=email,password=password,conpassword=conpassword,image=image)
          reg.save()
          my_use=User.objects.create_user(name,email,password)
          my_use.save()
          return redirect("login")
        #   if login_valide(email,conpassword,password):
              
        #       print("ragister successfull...")
        #       return render(request,"home/login.html")
        #   name=request.POST.get('name')
        #   print(email+password+conpassword+name)
          
    return render(request,"travel/home/register.html" )

def bookingtour(request):
    if request.method=="POST":
        #name=User.username
        name=request.POST.get('destination')
        checkin=request.POST.get('checkin')
        checkout=request.POST.get('checkout')
        adults=int(request.POST.get('adults'))
        children=int(request.POST.get('children'))
        roomtype=request.POST.get('roomtype')
        adharcard=request.POST.get('adharcard')
        phone=request.POST.get('phonenumbr')
        Special_Requests=request.POST.get('specialrequests')
        user_name=request.POST.get('user_name')
        amount=request.POST.get('amount')
        book_id = str(uuid.uuid4())
        book=booking(booking_id=book_id,place_name=name,user_name=user_name,Mobie_number=phone,Adhar_card=adharcard,date_arrivale=checkin,date_return=checkout,adults_kids=children,Room_type=roomtype,Special_Requests=Special_Requests,amount=amount) 
        book.save()
        Travelers=(children)+(adults)
        book_detai={
        'place_name':name,
        'date_arrivale':checkin,
        'adults_kids':Travelers,
       }
        pack=package.objects.all()
        request.session['place']=name
        request.session['in']=checkin
        request.session['out']=checkout
        request.session['guest']=Travelers
        request.session['booking_id']=book_id
        user=request.user
        return render(request,'home/payment.html',{'book_detai':book_detai,'pack':pack,'user':user})
    place=request.GET.get('place_name')
    return render(request,"home/booking.html",{'place':place})

def bookingcon(request):
     name=request.session['place']
     checkin=request.session['in']
     checkout=request.session['out']
     Travelers=request.session['guest']
     booking_id= request.session['booking_id']
     pack=package.objects.all().filter(place_name=name)
     return render(request,"home/booking-confirmation.html",{ 'name':name,
        'checkin':checkin,
        'checkout':checkout,
        'Travelers':Travelers,
        'booking_id':booking_id,
        'pack':pack})
   
def payment_tour(request):
       
    return render(request,"travel/home/payment.html" )  

def profile_management(request):
     if request.method == 'POST':
        
        email = request.POST.get('email')
        image = request.FILES.get('image')
       
    
        # Save image if uploaded
        if image:
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            image_url = fs.url(filename)
        else:
            image_url = 'profile.jpg'  # default image path in media folder
           
        user=request.user
        u=User.objects.get(username=user.username)
       
        u.email=email
        u.save()
        user = ragister.objects.get(name=user.username)
        user.email_id = email
        user.image=image_url
        user.save()
        return redirect('profile')  # redirect to login or home page
     return render(request,"travel/home/profile-management.html" )

# image nu baki che
def profile(request):

    image=request.POST.get('user_img')
    user_name=request.GET.get('user_name')
    reg=ragister.objects.get(name="parth_ramanujj")
    reg.image=image
    
    user_name=request.GET.get('user_name')
    book=booking.objects.all()
    user=request.user
    reg=ragister.objects.all().filter(name=user)
  
    return render(request,"travel/home/profile.html",{'book':book,'user':user,'reg':reg,'user_name':user_name})

def payment_history(request):
    return render(request,"travel/home/payment-history.html")

def place_info(request):
   
   att=Attractions.objects.all()
   place=request.GET.get('place_name')
   pack=package.objects.all()
   feed=Feedback.objects.all()  
   user=User.objects.all() 
   user=request.user
   return render(request,"travel/home/place_info.html",{'place':place,'pack':pack,'att':att,'feed':feed,'user':user})


def superadmin (request):
    pay=payment.objects.all()
    book=booking.objects.all()
    pack=package.objects.all()
    rate=Feedback.objects.all()
    reg=ragister.objects.all()
    user=User.objects.all()
    hotels=hotel.objects.all()
    total_users = User.objects.count()
    total_bookings = booking.objects.count()
    total_rating = Feedback.objects.count()
    
    total_amount=0
    for p in pay:
     total_amount += p.amount 
    
    total_rating1=0 
    for f in rate:
      total_rating1 += f.rating
    avg_rating=total_rating1/total_rating   
    return render(request,"travel/admin/admin.html",{'pay':pay,'num':range(1, total_users),'book':book,'pack':pack,'rat':rate,'reg':reg,'user':user,'hotels':hotels,'total_users':total_users,
        'total_bookings':total_bookings,
        'total_amount':total_amount,
        'avg_rating':avg_rating})
def Review(request):   
    if request.method=="POST":
        #Review_user=Feedback.objects.all()
        place_name=request.POST.get('place_name')
        Review_user=request.POST.get('review')
        star=request.POST.get('star')
        user_name=request.POST.get('name')
        r_date= date.today()
        image = request.FILES.get('image')
        print(image)    
        # Save image if uploaded
        if image:
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            image_url = fs.url(filename)
        else:
            image_url = 'profile.jpg'  # default image path in media folder
        print(image_url)   
        feedback=Feedback(package_name=place_name,rating=star,discription=Review_user,r_date=r_date,user_name=user_name,image=image_url)
        feedback.save()        
        feed=Feedback.objects.all()
        place=request.GET.get('place_name')  
        pack=package.objects.all()
        att=Attractions.objects.all()
        return render(request,"travel/home/place_info.html",{'feed':feed,'place':place,'pack':pack,'att':att})  
    else:
        pack=package.objects.all()
        user=User.objects.all()
        user_name=request.user
        place=request.GET.get('place_name')  
        reg= ragister.objects.all()
    return render(request,"travel/home/Review.html",{'user':user,'pack':pack,'place':place,'un':user_name,'reg':reg})     
    
def tourcondition(request):
    filepath = os.path.join('tour_and_travalling/templates/travel', 'tourcondition.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
#manage admin panal

def manageuser(request):
    if request.method == "POST":
          name=request.POST.get('customerName')
          email=request.POST.get('customerEmail')
          password=request.POST.get('pass')
          conpassword=request.POST.get('cpass')
          image=request.POST.get('image')
          reg=ragister(name=name,email_id=email,password=password,conpassword=conpassword,image=image)
          reg.save()
          my_use=User.objects.create_user(name,email,password)
          my_use.save()
          return redirect("index")
    return render(request,"travel/admin/manageuser.html")


def managehotel(request):
    
     if request.method == 'POST':
        name = request.POST.get('hotel_name')
        loc = request.POST.get('hotel_loc')
        price = request.POST.get('hotel_price')
        status = request.POST.get('status')

        # Optional: convert price to int
        try:
            price = int(price)
        except (ValueError, TypeError):
            price = None  # or handle error

        new_hotel = hotel.objects.create(
            hotel_name=name,
            hotel_loc=loc,
            hotel_price=price,
            status=status
        )
        new_hotel.save()
        return redirect('superadmin')  # Update this to your success page
    
     return render(request,"travel/admin/managehotel.html")


def managepackeg(request):
    if request.method == 'POST':
        place_image = request.FILES.get('place_image')
        image_gallary = request.FILES.get('image_gallary')
        place_name = request.POST.get('place_name')
        package_price = request.POST.get('package_price')
        package_name = request.POST.get('package_name')
        package_desc = request.POST.get('package_desc')

        package.objects.create(
            place_image=place_image,
            place_name=place_name,
            package_price=package_price,
            package_name=package_name,
            package_desc=package_desc,
            image_gallary=image_gallary
        )
        return redirect('superadmin') 
       
    return render(request,"travel/admin/managepackeg.html")


def managefeedback(request):
    return render(request,"travel/admin/managefeedback.html")
def addpack(request):
    if request.method == "POST":  
     print("in add pack")
    else:
       print(request.GET.get('packagename'))
        
    return render(request,"travel/admin/managepackeg.html")

def managepayment(request):
    
    return render(request,"travel/admin/managepayment.html")


def managerating(request):
    r_id=request.GET.get('id')
   
    rat=Feedback.objects.all()
    return render(request,"travel/admin/managerating.html",{'rat':rat,'r_id':int(r_id)})

def upi(request):
    # name=request.session['name']
    # pack=package.objects.all().filter(place_name=name)
    price=request.GET.get('price') 
    return render(request,"travel/home/upi.html",{'price':price})

    

def managedelete(request):
    r_id=request.GET.get('d_id')
    u_id=request.GET.get('id')
    p_id=request.GET.get('p_id')
    h_id=request.GET.get('h_id')
    b_id=request.GET.get('b_id')
    if r_id:
        rat=Feedback.objects.get(Rating_id=r_id)
        rat.delete()
    if u_id:
        print("in user delete")
        user = ragister.objects.get(user_id=u_id)
        user.delete()
    if p_id:
        print("in pack delete")
        p = package.objects.get(package_id=p_id)
        p.delete()
    if h_id:
        print("in hotel delete")
        h = hotel.objects.get(hotel_id=h_id)
        h.delete()   
    if b_id:
        print("in hotel delete")
        b= booking.objects.get(booking_id=b_id)
        b.delete()        
    
    return redirect("superadmin")

def showuserdata(request):
    r_id=request.GET.get('id')
    r_id=int(r_id)
    reg=ragister.objects.all().filter(user_id=r_id)
    
    return render(request,"travel/admin/showuserdata.html",{'reg':reg})

def showhotel(request):
    r_id=request.GET.get('id')
    r_id=int(r_id)
    hot=hotel.objects.all().filter(user_id=r_id)
    
    return render(request,"travel/admin/showuserdata.html",{'hot':hot})

def editpackeg(request):
    p_id=request.GET.get('p_id')
    if request.method == 'POST':
        
        if p_id:
            place_image = request.FILES.get('place_image')
            place_name = request.POST.get('place_name')
            package_price = request.POST.get('package_price')
            package_name = request.POST.get('package_name')
            package_desc = request.POST.get('package_desc')
            obj = package.objects.get(package_id=p_id)
            obj.place_image=place_image
            obj.place_name=place_name
            obj.package_price=package_price
            obj.package_name=package_name
            obj.package_desc=package_desc
            obj.save()
            return redirect('superadmin')
    obj = package.objects.all().filter(package_id=p_id)
    return render(request,"travel/admin/editpackeg.html",{'pack':obj})

def edithotel(request):
    h_id=request.GET.get('h_id')
    if request.method == 'POST':
        if h_id:
            name = request.POST.get('hotel_name')
            loc = request.POST.get('hotel_loc')
            price = request.POST.get('hotel_price')
            status = request.POST.get('status')
            obj=hotel.objects.get(hotel_id=h_id)
            obj.hotel_name=name
            obj.hotel_loc=loc
            obj.hotel_price=price
            obj.status=status
            obj.save()
        return redirect('superadmin')
    obj = hotel.objects.all().filter(hotel_id=h_id)
    return render(request,"travel/admin/edithotel.html",{'htl':obj})