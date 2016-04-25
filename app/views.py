
import os
import json
from app.image_getter import *
from flask import Flask, render_template, session, redirect, url_for, flash, request, jsonify
#from flask.ext.script import Manager
from werkzeug import secure_filename
from flask.ext.bootstrap import Bootstrap
#from flask.ext.moment import Moment
from sqlalchemy.sql import *
from flask_wtf.file import *
from flask.ext.uploads import UploadSet, IMAGES
from flask.ext.wtf import Form
from random import randint
from wtforms.validators import Required, NumberRange
from flask.ext.sqlalchemy import SQLAlchemy
from app.models import Member, Wish

from app import app
#from flask import render_template, request, redirect, url_for
app.config['SECRET_KEY'] = 'hard to guess string'

db = SQLAlchemy(app)




###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return app.send_static_file('index.html')
    #return render_template('index.html')

@app.route('/api/thumbnail/process', methods=['GET'])
def selImage():
	url = request.args.get('url')
	data = imageget(url)
	return data;
	
@app.route('/api/user/register', methods=['POST'])
def regUser():
	data= json.loads(request.data.decode())
	emailaddr= data["email"]
	password= data["password"]
	username= data["username"]
	#uid = randint(600000000,699999999)
	user = Member.query.filter_by(email=emailaddr).first()
	if user is None:
		while True:
                	uid = randint(620000000,629999999)
                	if not db.session.query(exists().where(Member.userid == uid)).scalar():
                	    	break
		member=Member(uid,emailaddr,password,username)
		db.session.add(member)
		db.session.commit()
		return jsonify (error="null",data={"user":{ "id": uid,"email": emailaddr,"name": username}},message= "Success")
	else:
		return jsonify (error="1",data={},message= "Email already in use")
	return jsonify ()
	
@app.route('/api/user/login', methods=['POST'])
def usrLogin():
	data= json.loads(request.data.decode())
	emailaddr= data["email"]
	password= data["password"]
	user = Member.query.filter_by(email=emailaddr).first()
	passw = user.password
	if user is None:
		return jsonify (error="1",data={},message= "Bad user name or password")
	elif  password == passw:	
		return jsonify (error="null",data={"user":{ "id": user.userid,"email": user.email,"name": user.uname}},message= "Success")
	elif  password != passw:	
		return jsonify (error="1",data={},message= "Bad user name or password")
	

@app.route('/api/user/<usrID>/wishlist', methods=['POST','GET'])
def shwList(usrID):
	if request.method == "POST":
		data= json.loads(request.data.decode())
		title= data["title"]
		description= data["description"]
		user= usrID
		url= data["url"]
		thumbnail= data["thumbnail"]
		wish= Wish(title,description,thumbnail,user,url)
		db.session.add(wish)
		db.session.commit()
		wishes = db.session.query(Wish).filter_by(user=usrID).all()
	 	wishlist = []
        	for wish in wishes:
            		wishlist.append({'title': wish.title,'description':wish.description,'url':wish.url,'thumbnail':wish.thumbnail})
        	if(len(wishlist)>0):
            		return jsonify({"error":"null","data":{"wishes":wishlist},"message":"Success"})
        	else:
            		return jsonify({"error":"1","data":{},"message":"No such wishlist exists"})
	elif request.method == "GET":
		wishes = db.session.query(Wish).filter_by(user=usrID).all()
	 	wishlist = []
        	for wish in wishes:
            		wishlist.append({'title': wish.title,'description':wish.description,'url':wish.url,'thumbnail':wish.thumbnail})
        	if(len(wishlist)>0):
            		return jsonify({"error":"null","data":{"wishes":wishlist},"message":"Success"})
        	else:
            		return jsonify({"error":"1","data":{},"message":"No such wishlist exists"})
	  
###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8888")
