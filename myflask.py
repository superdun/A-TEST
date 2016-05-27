#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template ,url_for,jsonify,request
from flask.ext.bootstrap import Bootstrap
import sqlite3,os,time 
from werkzeug import secure_filename
app = Flask(__name__)
bootstrap = Bootstrap(app)

UPLOAD_FOLDER = 'static/uploaded_pics'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
	return render_template('index.html') 

@app.route('/upload_pics')
def upload_pics():
	return render_template('index.html') 	

l_count=r_count=0
@app.route('/container_ajax')
def apply_ajax():
	global l_count,r_count
	back_to_front=[]
	db= sqlite3.connect('tst.db')
	cursor = db.cursor()
	if request.args.get('source')=='dow':
		for i in range(3):
			cursor.execute("select * from DJI where id=?" , (l_count+i,))
			result=cursor.fetchall()
			back_to_front.append(result)
			if len(result)==0:
				l_count=-3
		l_count+=3
	else:
		for i in range(3):
			cursor.execute("select * from IXIC where id=?" , (l_count+i,))
			result=cursor.fetchall()
			back_to_front.append(result)
			if len(result)==0:
				l_count=-3
		l_count+=3
		
	cursor.close()
	db.commit()
	db.close()
	return jsonify(back_to_front=back_to_front)
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS	
	
@app.route('/upload',methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			print app.config['UPLOAD_FOLDER']
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return 

	
if __name__ == '__main__':
	app.run(port=8080,debug=True)