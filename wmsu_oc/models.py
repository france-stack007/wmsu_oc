
from sqlalchemy.sql import func
from sqlalchemy import column, func
from . import db, marsh, app
from flask_login import UserMixin
from datetime import datetime
from marshmallow import Schema, fields


class Role(marsh.Schema):
    class Meta:
        fields = ('id','user_id','store_name','date_created')
    
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self,role,date_created):

        self.role = role
        self.date_created = date_created

class UserSchema(marsh.Schema):
    class Meta:
        fields = ('id', 'first_name','middle_name','last_name', 'sex', 'contact', 'email', 'password', 'user_type','role','image_url','code' ,'verify','date_created')

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    middle_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    sex = db.Column(db.String(255), nullable=False)
    contact = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(150), unique=True ,nullable=False)
    password = db.Column(db.String(255),nullable=False)
    user_type = db.Column(db.Integer, db.ForeignKey('role.id'))
    role = db.Column(db.String(255),nullable=False)
    image_url = db.Column(db.String(255),default='https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png')  # set default image URL
    code = db.Column(db.Integer)
    verify = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    

    def __init__(self, first_name,middle_name,last_name, sex, contact, email, password, user_type,role, image_url, code,verify,date_created):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.sex = sex
        self.contact = contact
        self.email = email
        self.password = password
        self.user_type = user_type
        self.role = role
        self.image_url = image_url
        self.code=code
        self.verify=verify
        self.date_created=date_created



class VendorSchema(marsh.Schema):
    class Meta:
        fields = ('id','user_id','store_name','gcash_no','gcash_name','date_created')
    
class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    store_name = db.Column(db.String(255), nullable=False)
    gcash_no = db.Column(db.Integer)
    gcash_name = db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self,user_id,store_name,gcash_no,gcash_name,date_created):

        self.user_id = user_id
        self.store_name=store_name
        self.gcash_no=gcash_no
        self.gcash_name=gcash_name
        self.date_created = date_created



    


class FoodSchema(marsh.Schema):
    class Meta:
        fields = ('id','food_name','price','status','category','image','vendor_id','date_created')
    
class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_name = db.Column(db.String(255), nullable=False)
    price=db.Column(db.Integer)
    status = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), default='https://i.ibb.co/T4D0vD7/334445509-1139125010112015-3116619608976503677-n.png')  # set default image URL
    vendor_id = db.Column(db.Integer)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self,food_name,price, status,category,image_url,vendor_id,date_created):

        self.food_name = food_name
        self.price = price
        self.status = status
        self.category=category
        self.image_url=image_url
        self.vendor_id=vendor_id
        self.date_created = date_created
        
        
        
class CartSchema(marsh.Schema):
    class Meta:
        fields = ('id','customer_id','food_name', 'store' ,'quantity','price','total','date_created')
    
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id=db.Column(db.Integer)
    food_name = db.Column(db.String(255), nullable=False)
    store = db.Column(db.String(255), nullable=False)
    quantity=db.Column(db.Integer)
    price=db.Column(db.Integer)
    total=db.Column(db.Integer)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self,customer_id,food_name,store,quantity, price,total,date_created):

        self.customer_id = customer_id
        self.food_name = food_name
        self.store = store
        self.quantity = quantity
        self.price = price
        self.total=total
        self.date_created = date_created



        
        
class DeliverySchema(marsh.Schema):
    class Meta:
        fields = ('id','track_no','customer_id','food_name','vendor','quantity','price','total','mop','location','response','food_ready','payment','complete','errand_id','date_created')
    
class Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_no=db.Column(db.Integer)
    customer_id=db.Column(db.Integer)
    food_name = db.Column(db.String(255), nullable=False)
    vendor = db.Column(db.String(255), nullable=False)
    quantity=db.Column(db.Integer)
    price=db.Column(db.Integer)
    total=db.Column(db.Integer)
    mop=db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    response=db.Column(db.String(255), nullable=False, default="Pending")
    mop=db.Column(db.String(255), nullable=False)
    food_ready=db.Column(db.String(255), nullable=False, default="No")
    payment=db.Column(db.String(255), nullable=False, default="No")
    complete=db.Column(db.Integer)
    errand_id=db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    
    def __init__(self,track_no,customer_id,food_name,vendor,quantity, price,total,mop,location,response,food_ready,payment,complete,errand_id,date_created):

        self.track_no = track_no
        self.customer_id = customer_id
        self.food_name = food_name
        self.vendor = vendor
        self.quantity = quantity
        self.price = price
        self.total=total
        self.mop=mop
        self.location=location
        self.response=response
        self.food_ready=food_ready
        self.payment=payment
        self.complete=complete
        self.errand_id=errand_id
        self.date_created = date_created


class Complete_DeliverySchema(marsh.Schema):
    class Meta:
        fields = ('id','track_no','customer_id','food_name','vendor','quantity','price','total','mop','payment','location','response','food_ready','payment_stat','complete','errand_id','date_created')
    
class Complete_Delivery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_no=db.Column(db.Integer)
    customer_id=db.Column(db.Integer)
    food_name = db.Column(db.String(255), nullable=False)
    vendor = db.Column(db.String(255), nullable=False)
    quantity=db.Column(db.Integer)
    price=db.Column(db.Integer)
    total=db.Column(db.Integer)
    mop=db.Column(db.String(255), nullable=False)
    payment=db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    response=db.Column(db.String(255), nullable=False)
    food_ready=db.Column(db.String(255), nullable=False)
    payment_stat=db.Column(db.String(255), nullable=False, default="No")
    complete=db.Column(db.Integer)
    errand_id=db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self,track_no,customer_id,food_name,vendor,quantity, price,total,mop,payment,location,response,food_ready,payment_stat,complete,errand_id,date_created):

        self.track_no = track_no
        self.customer_id = customer_id
        self.food_name = food_name
        self.vendor = vendor
        self.quantity = quantity
        self.price = price
        self.total=total
        self.mop=mop
        self.payment=payment
        self.location=location
        self.response=response
        self.food_ready=food_ready
        self.payment_stat=payment_stat
        self.complete=complete
        self.errand_id=errand_id
        self.date_created = date_created
        
        
class FeeSchema(marsh.Schema):
    class Meta:
        fields = ('id','fees','date_created')
    
class Fee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fees=db.Column(db.Integer)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self,fees,date_created):

        self.fees = fees
        self.date_created = date_created
        

class RemittanceSchema(marsh.Schema):
    class Meta:
        fields = ('id','track_no','vendor_name','total','mod','payment','refereance','errand','date_created')
    
class Remittance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_no=db.Column(db.Integer)
    vendor_name=db.Column(db.String(255), nullable=False)
    total=db.Column(db.Integer)
    mop=db.Column(db.String(255), nullable=False)
    payment=db.Column(db.String(255), nullable=False)
    refereance=db.Column(db.Integer)
    errand=db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self,track_no,vendor_name,total,mop,payment,refereance,errand,date_created):

        self.track_no = track_no
        self.vendor_name = vendor_name
        self.total = total
        self.mop = mop
        self.payment = payment
        self.refereance = refereance
        self.errand = errand
        self.date_created = date_created
        
        
class Errand_sales(marsh.Schema):
    class Meta:
        fields = ('id','track_no','total','mod','payment','errand','date_created')

class Errand_sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track_no=db.Column(db.Integer)
    total=db.Column(db.Integer)
    mop=db.Column(db.String(255), nullable=False)
    payment=db.Column(db.String(255), nullable=False)
    errand=db.Column(db.String(255), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self,track_no,total,mop,payment,errand,date_created):


        self.track_no = track_no
        self.total = total
        self.mop = mop
        self.payment = payment
        self.errand = errand
        self.date_created = date_created
        
        
                



    


