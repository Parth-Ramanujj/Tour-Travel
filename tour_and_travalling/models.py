from datetime import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#1
class user_login(models.Model):
  srno=models.AutoField(primary_key=True,auto_created=True)
  email_id=models.CharField(max_length=40)
  password=models.CharField(max_length=20)
def __str__(self):
  return self.name
# Create your models here.

#2
class ragister(models.Model):
  user_id=models.AutoField(primary_key=True,auto_created=True)
  name=models.CharField(max_length=20)
  email_id=models.CharField(max_length=40)
  password=models.CharField(max_length=20)
  conpassword=models.CharField(max_length=20)
  join_date=models.DateField(default=timezone.now)
  image = models.ImageField(upload_to='profile_images/', null=True, default='profile.jpg')

 
  def __str__(self):
   return self.name 
    
  #3
class booking(models.Model):
    User_id=models.AutoField(primary_key=True,auto_created=True)
    booking_id=models.CharField(max_length=100,unique=True,null=False)
    place_name=models.CharField(max_length=40,null=True)
    user_name=models.CharField(max_length=30,null=False)
    Mobie_number=models.CharField(max_length=15,null=False)
    Adhar_card=models.CharField(max_length=12,null=False)
    date_arrivale=models.CharField(max_length=30,null=False)
    date_return=models.CharField(max_length=30,null=False)
    adults_kids=models.CharField(max_length=10,null=False)
    Room_type=models.CharField(max_length=30,null=False)
    Special_Requests=models.TextField(max_length=50)
    amount=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
       return self.place_name
    
    #4
# class package(models.Model):
#       package_id=models.AutoField(primary_key=True,auto_created=True)
#       place_image=models.CharField(max_length=40,null=False)
#       place_name=models.CharField(max_length=40,null=False)
#       package_price=models.IntegerField(null=False)
#       package_name=models.CharField(max_length=40,null=False)
#       package_desc=models.CharField(max_length=500,null=True)
#       image_gallary=models.CharField(max_length=100,null=False)
    

class package(models.Model):
    package_id = models.AutoField(primary_key=True)
    place_image =models.ImageField(upload_to='places/') # Or models.ImageField(upload_to='places/') if storing images
    place_name = models.CharField(max_length=40)
    package_price = models.IntegerField()
    package_name = models.CharField(max_length=40)
    package_desc = models.TextField(null=True, blank=True)
    image_gallary =models.ImageField(upload_to='gallery/')  # Or models.ImageField(upload_to='gallery/') if using images

    def __str__(self):
        return self.place_name

      # def __str__(self):
      #  return self.place_name
      
      #5
class payment(models.Model):
        payment_id=models.AutoField(primary_key=True,auto_created=True)
        user_id=models.CharField(max_length=100,unique=True,null=False)
        package_id=models.CharField(max_length=100,unique=True,null=False)
        amount=models.IntegerField(null=True)
        payment_type=models.CharField(max_length=50,null=False)
        
        def __str__(self):
         return self.payment_type
        #6
        
class Feedback(models.Model):
        Rating_id=models.AutoField(primary_key=True,auto_created=True)
        user_name=models.CharField(max_length=50,null=True)
        package_name=models.CharField(max_length=50,null=True)
        rating=models.IntegerField(null=True)
        discription=models.CharField(max_length=500,null=True)
        r_date=models.DateField(default=timezone.now,null=True)
        image = models.ImageField(upload_to='profile_images/', null=True, default='profile.jpg')
        def __str__(self):
         return self.package_name
        
class Attractions(models.Model):
  att_id=models.AutoField(primary_key=True,auto_created=True)
  place_name=models.CharField(max_length=40,null=True)
  att_name=models.CharField(max_length=40,null=False)
  att_image=models.CharField(max_length=80,null=False)
  att_desc=models.CharField(max_length=500,null=True)
  
        
  def __str__(self):
       return self.att_name
     
     
class hotel(models.Model):
  hotel_id=models.AutoField(primary_key=True,auto_created=True)
  hotel_name=models.CharField(max_length=40,null=True)
  hotel_loc=models.CharField(max_length=40,null=True)
  hotel_price=models.IntegerField(null=True)
  status=models.CharField(max_length=40,null=True)
  
  def __str__(self):
       return self.hotel_name