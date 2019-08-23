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
		create_query = ''.join(f.readlines())
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


#@app.route('/')
#def index():
	#return render_template('index.html')


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


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():

	if request.method == 'POST':
		schoolname = request.form.get('schoolname')
		standard = request.form.get('standard')
		name = request.form.get('name')
		numbers = request.form.get('numbers')
		code = request.form.get('code')
		gender = request.form.get('gender')
		dob = request.form.get('dob')
		age = request.form.get('age')
		immu = request.form.getlist('immu')
		immu = ','.join(immu)
		disease = request.form.getlist('disease')
		disease = ','.join(disease)
		sick = request.form.get('sick')
		food = request.form.get('food')
		meals = request.form.get('meals')
		junk = request.form.get('junk')
		water = request.form.get('water')
		breakfast = request.form.getlist('breakfast')
		breakfast = ','.join(breakfast)
		lunch = request.form.getlist('lunch')
		lunch = ','.join(lunch)
		snacks = request.form.getlist('snacks')
		snacks = ','.join(snacks)
		dinner = request.form.get('dinner')
		height = request.form.get('height')
		magnitude = request.form.get('magnitude')
		Rate = request.form.get('Rate')
		Rates = request.form.get('Rates')
		skin = request.form.get('skin')
		head = request.form.get('head')
		ear = request.form.get('ear')
		nose = request.form.get('nose')
		hearing = request.form.get('hearing')
		lymph = request.form.get('lymph')
		CVS = request.form.get('CVS')
		CNS = request.form.get('CNS')
		GIT = request.form.get('GIT')
		general = request.form.get('general')
		tonsil = request.form.get('tonsil')
		allergy = request.form.get('allergy')
		screen = request.form.get('screen')
		breathing = request.form.get('breathing')
		speech = request.form.get('speech')
		bleed = request.form.get('bleed')
		BT = request.form.get('BT')
		paediatric = request.form.getlist('paediatric')
		paediatric = ','.join(paediatric)
		carbohydrates = request.form.get('carbohydrates')
		minerals = request.form.get('minerals')
		Fats = request.form.get('Fats')
		Protein = request.form.get('Protein')
		vitamins = request.form.get('vitamins')
		undernourished = request.form.get('undernourished')
		overfed = request.form.get('overfed')
		obese = request.form.get('obese')
		fibre = request.form.get('fibre')
		nutritional = request.form.get('nutritional')
		answers = request.form.get('answers')
		diet = request.form.getlist('diet')
		diet = ','.join(diet)
		brush_twice = request.form.get('brush_twice')
		mouthwash = request.form.get('mouthwash')
		tongue = request.form.get('tongue')
		toothpaste = request.form.get('toothpaste')
		teeth = request.form.getlist('teeth')
		teeth = ','.join(teeth)
		fill = request.form.getlist('fill')
		fill = ','.join(fill)
		filled = request.form.getlist('filled')
		filled = ','.join(filled)
		fluorosis = request.form.get('fluorosis')
		gingivitis = request.form.get('gingivitis')
		malocclusion = request.form.get('malocclusion')
		calculus = request.form.get('calculus')
		stains = request.form.get('stains')
		coated = request.form.get('coated')
		gums = request.form.get('gums')
		swelling = request.form.get('swelling')
		sensitivity = request.form.get('sensitivity')
		TMJ = request.form.get('TMJ')
		ans = request.form.get('ans')
		dental = request.form.getlist('dental')
		dental = ','.join(dental)
		prob = request.form.get('prob')
		probs = request.form.get('probs')
		ye = request.form.get('ye')
		nots = request.form.get('nots')
		eye = request.form.getlist('eye')
		eye = ','.join(eye)
		eyes = request.form.getlist('eyes')
		eyes = ','.join(eyes)
		remark = request.form.getlist('remark')
		remark = ','.join(remark)
		opthal = request.form.get('opthal')
		psychological = request.form.get('psychological')
		psych = request.form.get('psych')
		psy = request.form.get('psy')
		ps = request.form.get('ps')
		nature = request.form.get('nature')
		intelligence = request.form.get('intelligence')
		NV = request.form.get('NV')
		attention = request.form.get('attention')
		memory = request.form.get('memory')
		motor = request.form.get('motor')

		conn = get_db()
		cur = conn.cursor()
		try:
			query = """INSERT INTO students(schoolname, standard, name,
					   numbers, code, gender, DOB, age, immu, disease, sick,
					   food, meals, junk, water, breakfast, lunch, snacks,
					   dinner, height, magnitude, Rate, Rates, skin, head, ear,
					   nose, hearing, lymph, CVS, CNS, GIT, general, tonsil,
					   allergy, screen, breathing, speech, bleed, BT, paediatric,
					   carbohydrates, minerals, Fats, Protein, vitamins,
					   undernourishhed, overfed, obese, fibre, nutritional,
					   answers, diet, brush_twice, mouthwash, tongue, toothpaste,
					   teeth, fill, filled, fluorosis,gingivitis, malocclusion,
					   calculus, stains, coated, gums, swelling, sensitivity, 
					   TMJ, ans, dental, prob, probs, ye, nots, eye, eyes,
					   remark, opthal, psychological, psych, psy, ps, nature,
					   intelligence, NV, attention, memory, motor) VALUES ( ? ,
					   ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? ,
					   ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? ,
					   ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? ,
					   ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? ,
					   ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? ,
					   ? , ? , ? , ?, ? , ? , ? , ? , ? , ? , ? , ? , ? , ? ,
					   ?, ?, ?, ?)"""
			cur.execute(query, (schoolname, standard, name, numbers, code,
							    gender, dob, age, immu, disease, sick, food,
								meals, junk, water, breakfast, lunch, snacks,
								dinner, height, magnitude, Rate, Rates, skin,
								head, ear, nose, hearing, lymph, CVS, CNS, GIT,
								general, tonsil, allergy, screen, breathing,
								speech, bleed, BT, paediatric, carbohydrates,
								minerals, Fats, Protein, vitamins,
								undernourished,overfed, obese, fibre,
								nutritional, answers, diet, brush_twice,
								mouthwash, tongue, toothpaste, teeth, fill,
								filled, fluorosis, gingivitis,
								malocclusion, calculus, stains, coated, gums,
								swelling, sensitivity, TMJ, ans, dental, prob,
								probs, ye, nots, eye, eyes, remark, opthal,
								psychological, psych, psy, ps, nature,
								intelligence, NV, attention, memory, motor))

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
