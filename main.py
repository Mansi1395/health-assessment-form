import os
import sqlite3
from sqlite3 import Error
from flask import Flask, render_template , g, flash, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy




import pygal

app = Flask(__name__)
DATABASE = "./database.db"
CREATE_QUERY_FILE = "healthform.sql"

if not os.path.exists(DATABASE):
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	with open(CREATE_QUERY_FILE, 'r') as f:
		create_query = f.readlines()
		print(create_query)
	cur.execute(create_query)
	conn.commit()
	conn.close()


def get_db():
	db = getattr(g, '_database', None)
	if not db:
		db = g._database = sqlite3.connect(DATABASE)
	return db


@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db:
		db.close()


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/send', methods=['GET', 'POST'])
def reply():
	if request.method == 'POST':
		school = request.form['schoolname']
		return render_template('index.html', schoolname=school)


#@app.route('/pygalexample/')
#def pygalexample graph = pygal.Pie()
	#graph.title = 'PERCENTAGE OF STUDENTS WHO REQUIRE FURTHER CONSULTATION'
	#graph.add('Yes', 25)
	#graph.add('No', 75)
	#graph_data = graph.render_data_uri()
	#return render_template('graphing.html', graph_data=graph_data)


@app.route('/enternew')
def new_student():
	return render_template('index.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():

	if request.method == 'POST':
		schoolname = request.form['schoolname']
		standard = request.form['standard']
		name = request.form['name']
		numbers = request.form['numbers']
		code = request.form['code']
		gender = request.form['gender']
		dob = request.form['dob']
		age = request.form['age']
		immu = request.form.getlist['immu']
		disease = request.form.getlist['disease']
		sick = request.form['sick']
		food = request.form['food']
		meals = request.form['meals']
		junk = request.form['junk']
		water = request.form['water']
		breakfast = request.form.getlist['breakfast']
		lunch = request.form.getlist['lunch']
		snacks = request.form.getlist['snacks']
		dinner = request.form['dinner']
		height = request.form['height']
		magnitude = request.form['magnitude']
		Rate = request.form['Rate']
		Rates = request.form['Rates']
		skin = request.form.get['skin']
		head = request.form.get['head']
		ear = request.form.get['ear']
		nose = request.form.get['nose']
		hearing = request.form.get['hearing']
		lymph = request.form.get['lymph']
		CVS = request.form.get['CVS']
		CNS = request.form.get['CNS']
		GIT = request.form.get['GIT']
		general = request.form.get['general']
		tonsil = request.form['tonsil']
		allergy = request.form['allergy']
		times = request.form['times']
		breathing = request.form.get['breathing']
		speech = request.form.get['speech']
		bleed = request.form.get['bleed']
		BT = request.form.get['BT']
		paediatric = request.form.getlist['paediatric']
		carbohydrates = request.form.get['carbohydrates']
		minerals = request.form.get['minerals']
		Fats = request.form.get['Fats']
		Protein = request.form.get['Protein']
		vitamins = request.form.get['vitamins']
		undernourished = request.form.get['undernourished']
		overfed = request.form.get['overfed']
		obese = request.form.get['obese']
		fibre = request.form.get['fibre']
		nutrtional = request.form.get['nutritional']
		answers = request.form['answers']
		diet = request.form.getlist['diet']
		brush_twice = request.form.get['brush_twice']
		mouthwash = request.form.get['mouthwash']
		tongue = request.form.get['tongue']
		toothpaste = request.form.get['toothpaste']
		teeth = request.form.get['teeth']
		fill = request.form.get['fill']
		filled = request.form.get['filled']
		fluorosis = request.form.get['fluorosis']
		gingivitis = request.form.get['gingivitis']
		malocclusion = request.form.get['malocclusion']
		calculus = request.form.get['calculus']
		stains = request.form.get['stains']
		coated = request.form.get['coated']
		gums = request.form.get['gums']
		swelling = request.form.get['swelling']
		sensitivity = request.form.get['sensitivity']
		TMJ = request.form.get['TMJ']
		ans = request.form['ans']
		dental = request.form.getlist['dental']
		prob = request.form['prob']
		probs = request.form['probs']
		ye = request.form['ye'] 
		nots = request.form['nots']
		eye = request.form.getlist['eye']
		eyes = request.form.getlist['eyes']
		remark = request.form.getlist['remark']
		opthal = request.form['opthal']
		psychological = request.form['psychological']
		psych = request.form['psych']
		psy = request.form['psy']
		ps = request.form['ps']
		nature = request.form['nature']
		intelligence = request.form.get['intelligence']
		NV = request.form.get['NV']
		attention = request.form.get['attention']
		memory = request.form.get['memory']
		motor = request.form.get['motor']

		conn = get_db()
		cur = conn.cursor()
		try:
			cur.execute("INSERT INTO students(schoolname, standard, name, numbers, code, gender, dob, age, immu, disease, sick, food, meals, junk, water, breakfast, lunch, snacks, dinner, height, magnitude, rate, rates, norma, abnorma, tonsil, allergy, normal, abnormal, paediatric, answer, norm, abn, nor, af, answers, diet, nom, an, teeth, fill, filled, dent, den, ans, dental, prob, probs, ye, nots, eye, eyes, remark, opthal, psychological, psych, psy, ps, nature, motor, learning, learn) VALUES ( ? , ? , ?, ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? )", (schoolname, standard, name, numbers, code, gender, dob, age, immu, disease, sick, food, meals, junk, water, breakfast, lunch, snacks, dinner, height, magnitude, rate, rates, norma, abnorma, tonsil, allergy, normal, abnormal, paediatric, answer, norm, abn, nor, af, answers, diet, nom, an, teeth, fill, filled, dent, den, ans, dental, prob, probs, ye, nots, eye, eyes, remark, opthal, psychological, psych, psy, ps, nature, motor, learning, learn))
			print("Inserted successfully")
			conn.commit()
		except:
			conn.rollback()
			raise RuntimeError("Error while insertion")
	return render_template("index.html")


@app.route('/list')
def list():
	conn = sqlite3.connect(DATABASE)
	cur = conn.cursor()
	conn.row_factory = sqlite3.Row    
	cur.execute("select * from students")
	rows = cur.fetchall()
	conn.commit()
	conn.close()

	return render_template("list.html", rows=rows)





if __name__ == "__main__":
	app.run(debug = True)
