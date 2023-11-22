from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify, make_response, session, send_from_directory
from flask_login import login_required, current_user
from .models import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import delete
from sqlalchemy import select, asc,desc
import datetime
from datetime import datetime, date
import json
from tkinter import Y
from flask import Flask, request, jsonify, render_template
import json
from os import path
import os
from flask_mail import Mail, Message
import random
import calendar
import smtplib
import base64
import re
from sqlalchemy import or_, and_




USER_CONTENT_FOLDER = 'usercont'
if not os.path.exists(USER_CONTENT_FOLDER):
    os.path.makedirs(USER_CONTENT_FOLDER)
    print("User content folder generated.")


_route_customer = Blueprint('_route_customer', __name__)


@_route_customer.route('/index')
@login_required
def dashboard():
    return '1'


flask_app = Flask(__name__) #Initialize flask_app

# ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg' }

@flask_app.route("/")
def Home():
    return render_template("index.html")


def check_email_with_domain(email, domain):
    # Extract the domain from the email
    email_domain = email.split('@')[-1]

    # Check if the email domain matches the specified domain
    return email_domain == domain

@_route_customer.route('/registration', methods=['POST'])
def registration():
     
    try:
        date = datetime.now()
        user = User.query.filter_by(email=request.form['email_add']).count()
        msg=''
        
        # Example usage
        email_to_check = request.form['email_add']
        if check_email_with_domain(email_to_check, 'wmsu.edu.ph'):
            if user==0:
                new_user = User(request.form['firstname'], request.form['mi'], request.form['lastname'],request.form['lastname'],request.form['contact'],request.form['email_add'], generate_password_hash(request.form['pass_word'], method="sha256"), 1,"customer", None, 0,0,date)
                db.session.add(new_user)
                db.session.commit()
                msg='success'
            else: 
                msg='exist'
        else:
            msg='invalid'
        
        return render_template("index.html",msg=msg)
    except:
        return render_template("index.html")


@_route_customer.route('/customer_login')
def customer_login():
     
    try:
       
       
            
        return render_template("Customer/customer_login.html")
            
    except:
        return render_template("index.html")


@_route_customer.route('/login',  methods=['POST','GET'])
def login():
     
    try:

        msg=''
        customer = User.query.filter_by(email=request.form['email_add'],role='customer').first()
        
        record = db.session.query(User, Vendor).select_from(User).join(Vendor, User.id == Vendor.user_id).all()
        # record=User.query.filter(User.id==Vendor.user_id).all()
        
        data = User.query.filter(User.user_type == 3).all()
        print(customer)
        if customer == None:
            msg='none'
            return render_template("Customer/customer_login.html",msg=msg)
        
        elif check_password_hash(customer.password, request.form['pass_word']):
            
            return render_template("Customer/customer_page.html",record=record,customer=customer)
            
        else:
            msg='error'
            return render_template("Customer/customer_login.html",msg=msg)
            
    except:
        
        return render_template("Customer/customer_login.html")
    

@_route_customer.route('/customer_page', methods=['POST','GET'])
def customer_page():
     
    try:

       customer = User.query.filter(User.id==request.form['customer_id']).first()
       record = db.session.query(User, Vendor).select_from(User).join(Vendor, User.id == Vendor.user_id).all()
       return render_template("Customer/customer_page.html",record=record,customer=customer)
        
    except:
        return render_template("Customer/customer_page.html")


@_route_customer.route('/admin_route')
def admin_route():
     
    try:
       return redirect(url_for('_route_admin.admin_login'))
        
    except:
        return render_template("index.html")
    
@_route_customer.route('/add_to_cart',  methods=['POST','GET'])
def add_to_cart():
     
    try:
       vendor = Vendor.query.filter_by(id=request.form['vendor_id']).first()
       food = Food.query.filter_by(id=request.form['food_id']).first()
       customer = User.query.filter(User.id==request.form['customer_id']).first()
       return render_template("Customer/customer_cart.html", food=food,vendor=vendor,customer=customer)
    except:
        return render_template("index.html")

@_route_customer.route('/menu',  methods=['POST','GET'])
def menu():
     
    try:
       
    #    food = Food.query.filter_by(vendor_id=request.form['vendor_id']).all()
       vendor = Vendor.query.filter_by(id=request.form['vendor_id']).first()
       food = Food.query.filter(Food.vendor_id == vendor.user_id , Food.status == 'Available').all()
       customer = User.query.filter(User.id==request.form['customer_id']).first()

       return render_template("Customer/customer_menu.html",food=food,vendor=vendor,customer=customer)
    except:
       return render_template("Customer/customer_menu.html")
    

    
@_route_customer.route('/cart',  methods=['POST','GET'])
def cart():
     
    try:
       
       food = Food.query.filter_by(id=request.form['food_id']).first()
       food_quantity = int(request.form['food_quantity'])
       total=food.price * food_quantity
       date = datetime.now()
       vendor = Vendor.query.filter_by(id=request.form['vendor_id']).first()
       customer = User.query.filter(User.id==request.form['customer_id']).first()
       check=Cart.query.filter_by(food_name=food.food_name, store=vendor.store_name,customer_id=request.form['customer_id']).count()
       if check==1: 
           add=Cart.query.filter_by(food_name=food.food_name, store=vendor.store_name,customer_id=request.form['customer_id']).first()
           add.quantity= add.quantity + food_quantity
           add.total= add.quantity * add.price
           
       else:
           add_cart = Cart(customer.id, food.food_name,vendor.store_name , request.form['food_quantity'], food.price,total,date)    
           db.session.add(add_cart)
       db.session.commit()
       data = Food.query.all()
       food = Food.query.filter_by(vendor_id=request.form['vendor_id'], category ='Available').all()
       record = db.session.query(User, Vendor).select_from(User).join(Vendor, User.id == Vendor.user_id).all()
       return render_template("Customer/customer_page.html", record=record,vendor=vendor,food=food,customer=customer)
    except:
       return render_template("Customer/customer_cart.html")



@_route_customer.route('/customer_orderlist', methods=['POST','GET'])
def customer_orderlist():
     
    try:
    #    customer1 = request.args.get('customer_id')
       orderlist = Cart.query.filter(Cart.customer_id == request.form['customer_id']).all()
       item = len(orderlist)
       total_sum = sum(order.total for order in orderlist)
       total_qty = sum(order.quantity for order in orderlist)
       customer = User.query.filter(User.id==request.form['customer_id']).first()
       fee = Fee.query.first()
       return render_template("Customer/customer_orderlist.html", orderlist=orderlist,item=item,total_sum=total_sum,total_qty=total_qty,customer=customer,fee=fee)
        
    except:
         return render_template("Customer/customer_orderlist.html")
    
def generate_random_number():
    return random.randint(10000000, 99999999)


def generate_unique_number():
    while True:
        number = generate_random_number()
        # Check if the number already exists in the database
        # existing_number = NumberModel.query.filter_by(number=number).first()
        # if not existing_number:
        return number

    
@_route_customer.route('/track_order',  methods=['POST','GET'])
def track_order():
    try:
        loc = request.form['loc']
        mop = request.form['mop']
        data_to_copy = Cart.query.all() 
        number = generate_random_number()
        customer = User.query.filter_by(id=request.form['customer_id']).first()
        if mop== "COD":
            # Prepare a list of dictionaries with the data to be inserted into the Delivery table
            delivery_data = []
            for item in data_to_copy:
                delivery_data.append({
                    'track_no': number,
                    'customer_id': item.customer_id,
                    'food_name': item.food_name,
                    'vendor': item.store,
                    'quantity': item.quantity,
                    'price': item.price,
                    'total': item.total,
                    'location': loc,
                    'response': 'Pending',
                    'mop': mop,
                    'food_ready': 'no',
                    'payment': 'no',
                    'complete': 0,
                    'errand_id': 0,
                    'date_created': datetime.now()
                })

            # Use bulk_insert_mappings to insert the data in a single database operation
            db.session.bulk_insert_mappings(Delivery, delivery_data)
            user = User.query.filter_by(id=request.form['customer_id']).first()
        
            # Commit the changes
            db.session.commit()
            
            # db.session.query(Cart).delete()
            
            criteria = (Cart.customer_id == request.form['customer_id'])  # Example filter criteria

            # Create a query object and apply the filter
            query = db.session.query(Cart).filter(criteria)

            query.delete()
            # Commit the changes
            db.session.commit()
            
            delivery = Delivery.query.filter(Delivery.customer_id ==request.form['customer_id']).all()
            # Define your filter criteria using SQLAlchemy filters
            criteria = and_(Delivery.customer_id == request.form['customer_id'], Delivery.response == 'Accepted')

            # Create a query object and apply the filter
            query = db.session.query(db.func.sum(Delivery.total)).filter(criteria)
            total_sum = query.scalar()
            # total_sum = db.session.query(db.func.sum(Delivery.total)).scalar()
            delivery1 = Delivery.query.filter(Delivery.customer_id ==request.form['customer_id']).first()
            loc = delivery1.location
            mop = delivery1.mop

            food_ready=Delivery.query.filter(Delivery.customer_id ==request.form['customer_id'], Delivery.food_ready=='yes').count()
            food_ready1=Delivery.query.filter(Delivery.customer_id ==request.form['customer_id'], Delivery.food_ready=='yes').first()

            msg=''
            msg_fee=''
            fee1=Fee.query.first()
            if food_ready > 0 and food_ready1.payment == 'yes':
                msg='paymet_ready'
                if food_ready1.mop == 'COD':
                    msg_fee='cod3'

            
            elif food_ready > 0:
                msg='ready'
                if food_ready1.mop == 'COD':
                    msg_fee='cod'


        elif mop == 'pickup':
            # Prepare a list of dictionaries with the data to be inserted into the Delivery table
            delivery_data = []
            loc="pickup"
            for item in data_to_copy:
                delivery_data.append({
                    'track_no': number,
                    'customer_id': item.customer_id,
                    'food_name': item.food_name,
                    'vendor': item.store,
                    'quantity': item.quantity,
                    'price': item.price,
                    'total': item.total,
                    'location': loc,
                    'response': 'Pending',
                    'mop': mop,
                    'food_ready': 'no',
                    'payment': 'no',
                    'complete': 0,
                    'errand_id': 0,
                    'date_created': datetime.now()
                })

            # Use bulk_insert_mappings to insert the data in a single database operation
            db.session.bulk_insert_mappings(Delivery, delivery_data)
            user = User.query.filter_by(id=request.form['customer_id']).first()
        
            # Commit the changes
            db.session.commit()
            
            # db.session.query(Cart).delete()
            
            criteria = (Cart.customer_id == request.form['customer_id'])  # Example filter criteria

            # Create a query object and apply the filter
            query = db.session.query(Cart).filter(criteria)

            query.delete()
            # Commit the changes
            db.session.commit()
            
            delivery = Delivery.query.filter(Delivery.customer_id ==request.form['customer_id']).all()
            # Define your filter criteria using SQLAlchemy filters
            criteria = and_(Delivery.customer_id == request.form['customer_id'], Delivery.response == 'Accepted')

            # Create a query object and apply the filter
            query = db.session.query(db.func.sum(Delivery.total)).filter(criteria)
            total_sum = query.scalar()
            # total_sum = db.session.query(db.func.sum(Delivery.total)).scalar()
            delivery1 = Delivery.query.filter(Delivery.customer_id ==request.form['customer_id']).first()
            loc = delivery1.location
            mop = delivery1.mop

            food_ready=Delivery.query.filter(Delivery.customer_id ==request.form['customer_id'], Delivery.food_ready=='yes').count()
            food_ready1=Delivery.query.filter(Delivery.customer_id ==request.form['customer_id'], Delivery.food_ready=='yes').first()

            msg=''
            msg_fee=''
            fee1=Fee.query.first()
            if food_ready > 0 and food_ready1.payment == 'yes':
                msg='paymet_ready'
                if food_ready1.mop == 'COD':
                    msg_fee='cod3'

            
            elif food_ready > 0:
                msg='ready'
                if food_ready1.mop == 'COD':
                    msg_fee='cod'


        return render_template("Customer/customer_track_order.html",mop=mop,loc=loc,delivery=delivery,total_sum=total_sum , number=delivery1, customer=customer, msg=msg,msg_fee=msg_fee,fee1=fee1.fees)
        
    except:
        
        return render_template("Customer/customer_track_order.html")
    
    

@_route_customer.route('/track',  methods=['POST','GET'])
def track():
    try:
        
        
        customer = User.query.filter_by(id=request.form['customer_id']).first()
        delivery1 = Delivery.query.filter(Delivery.customer_id ==request.form['customer_id']).count()

        if delivery1>0:
            delivery = Delivery.query.filter(Delivery.customer_id ==request.form['customer_id']).all()
            # Define your filter criteria using SQLAlchemy filters
            criteria = and_(Delivery.customer_id == request.form['customer_id'], Delivery.response == 'Accepted')

            # Create a query object and apply the filter
            query = db.session.query(db.func.sum(Delivery.total)).filter(criteria)
            total_sum = query.scalar()
            # total_sum = db.session.query(db.func.sum(Delivery.total)).scalar()
            delivery1 = Delivery.query.filter(Delivery.customer_id ==request.form['customer_id']).first()
            loc = delivery1.location
            mop = delivery1.mop

            food_ready=Delivery.query.filter(Delivery.customer_id ==request.form['customer_id'], Delivery.food_ready=='yes').count()
            food_ready1=Delivery.query.filter(Delivery.customer_id ==request.form['customer_id'], Delivery.food_ready=='yes').first()
            msg=''
            msg_fee=''
            fee1=Fee.query.first()
            if food_ready > 0 and food_ready1.payment == 'yes':
                msg = 'payment_ready'
                if food_ready1.mop == 'COD':
                    msg_fee = 'cod3'

                        
            elif food_ready > 0:
                msg = 'ready'
                if food_ready1.mop == 'COD':
                    msg_fee = 'cod'




            return render_template("Customer/customer_track_order.html",mop=mop,loc=loc,delivery=delivery,total_sum=total_sum, number=delivery1,customer=customer,msg=msg,fee1=fee1.fees,msg_fee=msg_fee)
        return render_template("Customer/customer_track_order_empty.html",customer=customer)
        
    except:
        
        return render_template("Customer/customer_track_order.html")
    

@_route_customer.route('/delete_cart',  methods=['POST','GET'])
def delete_cart():
    
        
        # Create a delete query using the filter() method
        food=Cart.query.filter(Cart.id==request.form['food_id']).first()
        db.session.delete(food)
        db.session.commit()
        
        orderlist = Cart.query.filter(Cart.customer_id == request.form['customer_id']).all()
        item = Cart.query.count()
        total_sum = db.session.query(db.func.sum(Cart.total)).scalar()
        total_qty = db.session.query(db.func.sum(Cart.quantity)).scalar()
        customer = User.query.filter(User.id==request.form['customer_id']).first()
        fee = Fee.query.first()
        return render_template("Customer/customer_orderlist.html", orderlist=orderlist,item=item,total_sum=total_sum,total_qty=total_qty,customer=customer,fee=fee)



@_route_customer.route('/customer_profile',  methods=['POST','GET'])
def customer_profile():
        customer = User.query.filter(User.id==request.form['customer_id']).first()
        return render_template("Customer/customer_profile.html",customer=customer)


@_route_customer.route('/customer_transaction',methods=['POST','GET'])
def customer_transaction():
    date = datetime.now()
    customer = User.query.filter(User.id==request.form['customer_id']).first()
    customer1=Complete_Delivery.query.filter_by(customer_id=customer.id).first()
    customer2=Complete_Delivery.query.filter_by(customer_id=0).count()
    if customer2==0:
        
         new_del = Complete_Delivery("No Record",0,"No Record","No Record",0,0,0,"No Record","No Record","No Record","No Record","No Record","No Record",0,0,date)
         db.session.add(new_del)
         db.session.commit()
         remit_money=Remittance.query.filter_by(track_no="No Record").all()
    
    complete=Complete_Delivery.query.filter(Complete_Delivery.customer_id==customer.id).with_entities(Complete_Delivery.track_no).distinct().all()

    return render_template("Customer/customer_transaction.html",customer=customer,complete=complete)

@_route_customer.route('/customer_transaction_details',methods=['POST','GET'])
def customer_transaction_details():
    date = datetime.now()
    customer = User.query.filter(User.id==request.form['customer_id']).first()
    customer1=Complete_Delivery.query.filter_by(customer_id=customer.id).first()
    customer2=Complete_Delivery.query.filter_by(customer_id=0).count()
    if customer2==0:
        
         new_del = Complete_Delivery("No Record",0,"No Record","No Record",0,0,0,"No Record","No Record","No Record","No Record","No Record","No Record",0,0,date)
         db.session.add(new_del)
         db.session.commit()
         remit_money=Remittance.query.filter_by(track_no="No Record").all()
    
    complete=Complete_Delivery.query.filter(Complete_Delivery.customer_id==customer.id,Complete_Delivery.track_no==request.form['track_no']).all()

    return render_template("Customer/customer_transaction_details.html",customer=customer,complete=complete)


@_route_customer.route('/usercont/<path:file>')
def serve_usercont(file):
    return send_from_directory(os.path.abspath(USER_CONTENT_FOLDER), file)

def gen_random_fname(length = 32):
    src = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join([src[random.randint(0, len(src) - 1)] for x in range(0, length)])


def handle_profile_submition(file):
    if file.filename == '':
        return None
    fname = f"{gen_random_fname()}{os.path.splitext(file.filename)[1]}"
    file.save(os.path.join(USER_CONTENT_FOLDER, fname))
    return fname 


@_route_customer.route('/customer_profile_update',  methods=['POST','GET'])
def customer_profile_update():
        
        fname = None
        if 'file' in request.files:
            fname = handle_profile_submition(request.files['file'])
            if fname is None:
                print("error")
        customer = User.query.filter(User.id==request.form['customer_id']).first()

        customer.first_name=request.form['first_name']
        customer.last_name=request.form['last_name']
        customer.middle_name=request.form['middle_name']
        customer.contact=request.form['contact']
        customer.email=request.form['email']
        customer.password=generate_password_hash(request.form['password'])
        customer.image_url=f"/{USER_CONTENT_FOLDER}/{fname}"
        db.session.commit()
        return render_template("Customer/customer_profile.html",customer=customer)
    


