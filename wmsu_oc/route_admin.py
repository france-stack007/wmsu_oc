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


_route_admin = Blueprint('_route_admin', __name__)

flask_app = Flask(__name__) #Initialize flask_app

@_route_admin.route('/admin_page')
def admin_page():
    

    return render_template("Admin/admin_dashboard.html" )


@_route_admin.route('/admin_dashboard',  methods=['POST','GET'])
def admin_dashboard():
    
    vendor = db.session.query(User, Vendor).select_from(User).join(Vendor, User.id == Vendor.user_id).count()
    staff =User.query.filter(User.user_type==5).count()
    errand =User.query.filter(User.user_type==4).count()
    user_id = User.query.filter_by(id=request.form['user_id']).first()

    return render_template("Admin/admin_dashboard.html", vendor=vendor,staff=staff,errand=errand,user_id=user_id)


@_route_admin.route('/admin_login',  methods=['POST','GET'])
def admin_login():

    try:
        
        vendor = db.session.query(User, Vendor).select_from(User).join(Vendor, User.id == Vendor.user_id).count()
        staff =User.query.filter(User.user_type==5).count()
        errand =User.query.filter(User.user_type==4).count()
       
        user_id = User.query.filter_by(email=request.form['email_add']).first()
        
        if user_id.user_type==2:
            if check_password_hash(user_id.password, request.form['pass_word']):
                return render_template("Admin/admin_dashboard.html",vendor=vendor,staff=staff,errand=errand,user_id=user_id)
            else:
                msg='invalid'
                return render_template("Admin/admin_login.html",msg=msg)
        elif user_id.user_type==3:
            if check_password_hash(user_id.password, request.form['pass_word']):
                return redirect(url_for('_route_vendor.vendor_page',user_id=user_id.id))
            else:
                msg='invalid'
                return render_template("Admin/admin_login.html",msg=msg)
        elif user_id.user_type==4:
            if check_password_hash(user_id.password, request.form['pass_word']):
                return redirect(url_for('_route_errand.errand_page',user_id=user_id.id))
            else:
                msg='invalid'
                return render_template("Admin/admin_login.html",msg=msg)
        elif user_id.user_type==5:
            if check_password_hash(user_id.password, request.form['pass_word']):
                return redirect(url_for('_route_errand.errand_page'))
            else:
                msg='invalid'
                return render_template("Admin/admin_login.html",msg=msg)
        else:
            msg='invalid'
            return render_template("Admin/admin_login.html",msg=msg)
            
    except:
        return render_template("Admin/admin_login.html")


@_route_admin.route('/add_vendor',  methods=['POST','GET'])
def add_vendor():

    try:
       
        date = datetime.now()
        fname = None
        if 'file' in request.files:
            fname = handle_profile_submition(request.files['file'])
            if fname is None:
                print("error")

        image=f"/{USER_CONTENT_FOLDER}/{fname}"
        
        new_user = User(request.form['firstname'], request.form['mi'], request.form['lastname'],request.form['lastname'],request.form['contact'],request.form['email_add'], generate_password_hash(request.form['pass_word'], method="sha256"), 3, "vendor",image, 0,0,date)
        
        db.session.add(new_user)
        db.session.commit()
        
        details1 =User.query.filter(User.email==request.form['email_add']).first()
        details1.id
        vendor = Vendor(details1.id,request.form['store_name'],request.form['gcash_no'],request.form['gcash_name'],date)
        db.session.add(vendor)
        db.session.commit()
        user_id = User.query.filter_by(id=request.form['user_id']).first()
        vendor = db.session.query(User, Vendor).select_from(User).join(Vendor, User.id == Vendor.user_id).count()
        staff =User.query.filter(User.user_type==5).count()
        errand =User.query.filter(User.user_type==4).count()
        msg='success'
        return render_template("Admin/admin_dashboard.html",user_id=user_id,vendor=vendor,errand=errand,msg=msg)
            
    except:
        return render_template("Admin/admin_login.html")
    
@_route_admin.route('/add_staff',  methods=['POST','GET'])
def add_staff():

    try:
       
        date = datetime.now()

        fname = None
        if 'file' in request.files:
            fname = handle_profile_submition(request.files['file'])
            if fname is None:
                print("error")

        image=f"/{USER_CONTENT_FOLDER}/{fname}"
        
        new_user = User(request.form['firstname'], request.form['mi'], request.form['lastname'],request.form['lastname'],request.form['contact'],request.form['email_add'], generate_password_hash(request.form['pass_word'], method="sha256"), 5, "staff",image, 0,0,date)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('_route_admin.admin_dashboard'))
            
    except:
        return render_template("Admin/admin_login.html")
    
@_route_admin.route('/add_errand',  methods=['POST','GET'])
def add_errand():

    try:
       
        date = datetime.now()

        fname = None
        if 'file' in request.files:
            fname = handle_profile_submition(request.files['file'])
            if fname is None:
                print("error")

        image=f"/{USER_CONTENT_FOLDER}/{fname}"
        
        new_user = User(request.form['firstname'], request.form['mi'], request.form['lastname'],request.form['lastname'],request.form['contact'],request.form['email_add'], generate_password_hash(request.form['pass_word'], method="sha256"), 4, "errand",image, 0,0,date)
        db.session.add(new_user)
        db.session.commit()
        
        user_id = User.query.filter_by(id=request.form['user_id']).first()
        vendor = db.session.query(User, Vendor).select_from(User).join(Vendor, User.id == Vendor.user_id).count()
        staff =User.query.filter(User.user_type==5).count()
        errand =User.query.filter(User.user_type==4).count()
        return render_template("Admin/admin_dashboard.html",user_id=user_id,vendor=vendor,errand=errand)
            
    except:
        return render_template("Admin/admin_login.html")
    

@_route_admin.route('/transaction',  methods=['POST','GET'])
def transaction():

    try:
        return render_template("Admin/transaction_dashboard.html")
            
    except:
        return render_template("Admin/admin_login.html")
    
@_route_admin.route('/admin_transaction',  methods=['POST','GET'])
def admin_transaction():

    try:
        user_id = User.query.filter_by(id=request.form['user_id']).first()
        return render_template("Admin/admin_transaction.html",user_id=user_id)
            
    except:
        return render_template("Admin/admin_transaction.html")
    
    
@_route_admin.route('/admin_fee',  methods=['POST','GET'])
def admin_fee():    
    
    try:
        user_id = User.query.filter_by(id=request.form['user_id']).first()
        fe=Fee.query.first()
        return render_template("Admin/admin_fee.html",user_id=user_id,fe=fe)
            
    except:
        return render_template("Admin/admin_fee.html")
    

@_route_admin.route('/admin_vendor',  methods=['POST','GET'])
def admin_vendor():    
    
    try:
        vendor = db.session.query(User, Vendor).select_from(User).join(Vendor, User.id == Vendor.user_id).count()
        errand =User.query.filter(User.user_type==4).count()
        user_id = User.query.filter_by(id=request.form['user_id']).first()
        record = db.session.query(User, Vendor).select_from(User).join(Vendor, User.id == Vendor.user_id).all()

        
        return render_template("Admin/admin_dashboard_vendor.html",user_id=user_id,vendor=vendor,errand=errand,record=record)
            
    except:
        return render_template("Admin/admin_dashboard_vendor.html")

@_route_admin.route('/delete_vendor',  methods=['POST','GET'])
def delete_vendor():    
    
    try:
        vendor = db.session.query(User, Vendor).select_from(User).join(Vendor, User.id == Vendor.user_id).count()
        errand =User.query.filter(User.user_type==4).count()
        user_id = User.query.filter_by(id=request.form['user_id']).first()
        record = db.session.query(User, Vendor).select_from(User).join(Vendor, User.id == Vendor.user_id).all()
        
        store=Vendor.query.filter(Vendor.id==request.form['vendor_id']).first()
      
        db.session.delete(store)
       
       
        db.session.commit()
        return render_template("Admin/admin_dashboard_vendor.html",user_id=user_id,vendor=vendor,errand=errand,record=record)
            
    except:
        return render_template("Admin/admin_dashboard_vendor.html")
    
    

    
@_route_admin.route('/edit_fee',  methods=['POST','GET'])
def edit_fee():

    try:
        
        msg=''
        fe=Fee.query.first()
        count=Fee.query.count()
        date = datetime.now()
        if count== 0:
            edit = Fee(request.form['fee'],date)    
            db.session.add(edit)
        else: 
            fe.fees=request.form['fee']
            msg='edit'
        db.session.commit()
        user_id = User.query.filter_by(id=request.form['user_id']).first()
        return render_template("Admin/admin_fee.html",user_id=user_id,fe=fe,msg=msg)
            
    except:
        return render_template("Admin/admin_fee.html")
    

@_route_admin.route('/admin_profile',  methods=['POST','GET'])
def admin_profile():    
    
    try:
        user_id = User.query.filter_by(id=request.form['user_id']).first()
        
        return render_template("Admin/admin_profile.html",user_id=user_id)
            
    except:
        return render_template("Admin/admin_profile.html")

@_route_admin.route('/admin_profile_update',  methods=['POST','GET'])
def admin_profile_update():
        
        fname = None
        if 'file' in request.files:
            fname = handle_profile_submition(request.files['file'])
            if fname is None:
                print("error")
        user_id = User.query.filter(User.id==request.form['user_id']).first()

        user_id.first_name=request.form['first_name']
        user_id.last_name=request.form['last_name']
        user_id.middle_name=request.form['middle_name']
        user_id.contact=request.form['contact']
        user_id.email=request.form['email']
        user_id.password=generate_password_hash(request.form['password'])
        user_id.image_url=f"/{USER_CONTENT_FOLDER}/{fname}"
        db.session.commit()
        msg='edit'
        return render_template("Admin/admin_profile.html",user_id=user_id,msg=msg)
    
    
@_route_admin.route('/usercont/<path:file>')
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