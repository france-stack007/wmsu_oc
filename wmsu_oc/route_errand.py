from flask import Flask,Blueprint, render_template, request, flash, redirect, url_for, jsonify,send_from_directory, make_response, session
from flask_login import login_required, current_user
from .models import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import delete, desc, asc
from sqlalchemy import delete
from sqlalchemy import select
import json
from os import path
import os
from io import TextIOWrapper
import csv
import io
import random
import base64
import datetime
from datetime import datetime, date,timedelta


USER_CONTENT_FOLDER = 'usercont'
if not os.path.exists(USER_CONTENT_FOLDER):
    os.path.makedirs(USER_CONTENT_FOLDER)
    print("User content folder generated.")


_route_errand = Blueprint('_route_errand', __name__)

flask_app = Flask(__name__) #Initialize flask_app

@_route_errand.route('/errand_page')
def errand_page():

    user_id = request.args.get('user_id')
    
    errand=User.query.filter_by(id=user_id).first()

    deliveries = Delivery.query.filter(Delivery.response == 'Pending',Delivery.errand_id==0).with_entities(Delivery.track_no, Delivery.response).count()
    track=''
    if deliveries == 0:
        track = Delivery.query.with_entities(Delivery.track_no).filter(Delivery.mop=="COD",Delivery.errand_id==0).distinct().all()

    return render_template("Errand/errand_page.html",track=track,errand=errand)

@_route_errand.route('/errand_dashboard',methods=['POST','GET'])
def errand_dashboard():

    errand=User.query.filter_by(id=request.form['errand_id']).first()

    deliveries = Delivery.query.filter(Delivery.response == 'Pending',Delivery.errand_id==0).with_entities(Delivery.track_no, Delivery.response).count()
    track=''
    if deliveries == 0:
        track = Delivery.query.with_entities(Delivery.track_no).filter(Delivery.mop=="COD",Delivery.errand_id==0).distinct().all()

    return render_template("Errand/errand_page.html",track=track,errand=errand)


@_route_errand.route('/errand_view_details',methods=['POST','GET'])
def errand_view_details():
    errand=User.query.filter_by(id=request.form['errand_id']).first()
    order = Delivery.query.filter(Delivery.track_no == request.form['track_no'], Delivery.response=='Accepted').all()
    for order1 in order:
        order1.errand_id=request.form['errand_id']
    db.session.commit()
    return render_template("Errand/errand_view_details.html",order=order, track=request.form['track_no'],errand=errand)

@_route_errand.route('/errand_food_ready',methods=['POST','GET'])
def errand_food_ready():
    errand=User.query.filter_by(id=request.form['errand_id']).first()
    track = Delivery.query.filter(Delivery.track_no == request.form['track']).first()
    customer = User.query.filter(User.id == track.customer_id).first()

    records_to_update = Delivery.query.filter(Delivery.customer_id == customer.id).all()

    for record in records_to_update:
        record.food_ready = 'yes'
    
    # After making changes, commit the updates to the database.
    db.session.commit()

    return render_template("Errand/errand_food_ready.html",customer=customer,track=track,errand=errand)

@_route_errand.route('/errand_remittance',methods=['POST','GET'])
def errand_remittance():

    errand=User.query.filter_by(id=request.form['errand_id']).first()
    track = Delivery.query.filter(Delivery.track_no == request.form['track']).first()
    orderlist = Delivery.query.filter(Delivery.track_no == request.form['track'], Delivery.response=='Accepted').all()
    total_sum = sum(order.total for order in orderlist)
    
    customer = User.query.filter(User.id == track.customer_id).first()

    for orderlist1 in orderlist:
            orderlist1.payment = 'yes'
        # After making changes, commit the updates to the database.
    db.session.commit()
    
    

    return render_template("Errand/errand_remittance.html",track=track,total_sum=total_sum,customer=customer,errand=errand)

@_route_errand.route('/errand_sales',methods=['POST','GET'])
def errand_sales():
    
    
    errand=User.query.filter_by(id=request.form['errand_id']).first()
    sale = Errand_sales.query.filter(Errand_sales.errand == errand.id).with_entities(Errand_sales.track_no, Errand_sales.total,Errand_sales.mop).distinct().all()
    
    total_sum = sum(order.total for order in sale)
    
    return render_template("Errand/errand_sales.html",errand=errand,sale=sale,total_sum=total_sum)

@_route_errand.route('/errand_remittance_cut',methods=['POST','GET'])
def errand_remittance_cut():
    
    try:
        errand=User.query.filter_by(id=request.form['errand_id']).first()
        track = Delivery.query.filter(Delivery.errand_id == errand.id).first()
        orderlist = Delivery.query.filter(Delivery.errand_id == errand.id, Delivery.response=='Accepted').all()
        total_sum = sum(order.total for order in orderlist)
        
        customer = User.query.filter(User.id == track.customer_id).first()
        fe=Fee.query.first()
        
        
        return render_template("Errand/errand_remittance.html",track=track,total_sum=total_sum,customer=customer,errand=errand)
    
    except:
        date = datetime.now()
        search=User.query.filter_by(first_name="No Record",last_name="No Record",middle_name="No Record").count()

        if search== 0:
            new_user = User("No Record", "No Record", "No Record","No Record","No Record","No Record", "No Record", 5, "No Record",None, 0,0,date)
            new_del = Delivery("No Record",0,"No Record","No Record",0,0,0,"No Record","No Record","No Record","No Record","No Record",0,0,date)
            db.session.add(new_user)
            db.session.add(new_del)
            db.session.commit()
        
        
        track = Delivery.query.filter(Delivery.food_name == "No Record").first()
        orderlist = Delivery.query.filter(Delivery.response=='No Record').all()
        total_sum = sum(order.total for order in orderlist)

        for orderlist1 in orderlist:
            orderlist1.payment = 'yes'
        # After making changes, commit the updates to the database.
        db.session.commit()
        customer = User.query.filter(User.id == track.customer_id).first()
        

        return render_template("Errand/errand_remittance.html",track=track,total_sum=total_sum,customer=customer,errand=errand)
    

@_route_errand.route('/errand_transaction',methods=['POST','GET'])
def errand_transaction():
    errand=User.query.filter_by(id=request.form['errand_id']).first()

    return render_template("Errand/errand_transaction.html",errand=errand)


@_route_errand.route('/errand_remittance_1',methods=['POST','GET'])
def errand_remittance_1():
    errand=User.query.filter_by(id=request.form['errand_id']).first()
    track = Delivery.query.filter(Delivery.track_no == request.form['track']).first()
    orderlist = Delivery.query.filter(Delivery.track_no == request.form['track'], Delivery.response=='Accepted').all()
    total_sum = sum(order.total for order in orderlist)
    fe=Fee.query.first()
    total_sum=fe.fees + total_sum
    customer = User.query.filter(User.id == track.customer_id).first()

    return render_template("Errand/errand_remittance.html",track=track,total_sum=total_sum,customer=customer,errand=errand)


@_route_errand.route('/remit',methods=['POST','GET'])
def remit():
    
    track = Delivery.query.filter(Delivery.track_no == request.form['track_no']).first()
    errand=User.query.filter_by(id=request.form['errand_id']).first()
    payment=request.form['payment'] #gcash or cash
    
    orderlist = Delivery.query.filter(Delivery.track_no == request.form['track_no'], Delivery.response=='Accepted').all()
    total_sum = sum(order.total for order in orderlist)

    refereance=request.form['ref_no']
    if payment== "cash":
        refereance= "None"

    date = datetime.now()
    # Query to get unique vendors and their total sum for the given track number
    vendors_and_sums = db.session.query(Delivery.vendor, db.func.sum(Delivery.total).label('total_sum')).filter(Delivery.track_no == request.form['track_no']).group_by(Delivery.vendor).all()

    # Iterate over each vendor and total sum, and create a Remittance object
    for vendor_and_sum in vendors_and_sums:
        vendor = vendor_and_sum.vendor
        total_sum = vendor_and_sum.total_sum
        
    
        remit = Remittance(track.track_no, vendor, total_sum, track.mop, request.form['payment'], refereance, errand.first_name, date)

        # Add the Remittance object to the database session
        db.session.add(remit)

    # Commit all changes to the database
    msg='remit'
    db.session.commit()
    
    # data_to_copy = Delivery.query.filter(Delivery.track_no == track.track_no).all()
    # total_sum = sum(order.total for order in data_to_copy)

   
        # Prepare a list of dictionaries with the data to be inserted into the Delivery table
    # delivery_data = []
    # for item in data_to_copy:
    #     delivery_data.append({
    #         'track_no': item.track_no,
    #         'customer_id': item.customer_id,
    #         'food_name': item.food_name,
    #         'vendor': item.vendor,
    #         'quantity': item.quantity,
    #         'price': item.price,
    #         'total': item.total,
    #         'mop': item.mop,
    #         'payment': payment,
    #         'location': item.location,
    #         'reponse': item.response,
    #         'food_ready': item.food_ready,
    #         'payment_stat': item.payment,
    #         'complete': item.complete,
    #         'errand_id': item.errand_id,
    #         'date_created': datetime.now()
    #     })

        # Use bulk_insert_mappings to insert the data in a single database operation
        # db.session.bulk_insert_mappings(Complete_Delivery, delivery_data)
        # db.session.commit()
        
        # db.session.query(Cart).delete()
        
    # criteria = (Delivery.track_no == track.track_no)  

           
    # query = db.session.query(Delivery).filter(criteria)

    # query.delete()
            
    # db.session.commit()
            

    return render_template("Errand/errand_page.html",errand=errand,msg=msg)


@_route_errand.route('/usercont/<path:file>')
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