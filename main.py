from flask import Flask, render_template, request,flash,redirect, url_for
import sqlite3
from sqlite3 import Error
import pygal

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/send', methods = ['GET','POST'])
def reply():
	if request.method == 'POST':
		School = request.form['schoolname']
		return render_template('index.html',schoolname=schoolname)


@app.route('/pygalexample/')
def pygalexample():
		graph = pygal.Pie()
		graph.title = 'PERCENTAGE OF STUDENTS WHO REQUIRE FURTHER CONSULTATION'
		graph.add('Yes', 25)
		graph.add('No', 75)
		graph_data = graph.render_data_uri()
		return render_template('graphing.html',graph_data=graph_data)



@app.route('/enternew')
def new_student():
	return render_template('index.html')



@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():

	if request.method == 'POST':
		schoolname = request.form['schoolname']
		Standard = request.form['Standard']
		Name = request.form['Name']
		Numbers = request.form['Numbers']
		code = request.form['code']
		gender = request.form['gender']
		DOB = request.form['DOB']
		age = request.form['age']
		immu = request.form['immu']
		disease = request.form['disease']
		Sick = request.form['Sick']
		Food = request.form['Food']
		Meals = request.form['Meals']
		Junk = request.form['Junk']
		Water = request.form['Water']
		breakfast = request.form['breakfat']
		lunch = request.form['lunch']
		snacks = request.form['snacks']
		dinner = request.form['dinner']
		height = request.form['height']
		magnitude = request.form['magnitude']
		Rate = request.form['Rate']
		Rates = request.form['Rates']
		norma = request.form['norma']
		abnorma = request.form['abnorma']
		tonsil = request.form['tonsil']
		allergy = request.form['allergy']
		times = request.form['times']
		normal = request.form['normal']
		abnormal = request.form['abnormal']
		paediatric = request.form['paediatric']
		answer = request.form['answer']
		norm = request.form['norm']
		abn = request.form['abn']
		nor = request.form['nor']
		af = request.form['af']
		answers = request.form['answers']
		diet = request.form['diet']
		nom = request.form['nom']
		an = request.form['an']
		teeth = request.form['teeth']
		fill = request.form['fill']
		filled = request.form['filled']
		dent = request.form['dent']
		den = request.form['den']
		ans = request.form['ans']
		dental = request.form['dental']
		prob = request.form['prob']
		probs = request.form['probs']
		Ye = request.form['Ye'] 
		nots = request.form['nots']
		eye = request.form['eye']
		eyes = request.form['eyes']
		remark = request.form['remark']
		opthal = request.form['opthal']
		psychological = request.form['psychological']
		psych = request.form['psych']
		psy = request.form['psy']
		ps = request.form['ps']
		nature = request.form['nature']
		motor = request.form['motor']
		learning = request.form['learning']
		learn = request.form['learn']

		with sql.connect("database.db") as con:
			cur = con.cursor()
			cur.execute("INSERT INTO students(schoolname, Standard, Name, Numbers, code, gender, DOB, age, immu, disease, Sick, Food, Meals, Junk, Water, breakfast, lunch, snacks, dinner, height, magnitude, Rate, Rates, norma, abnorma, tonsil, allergy, normal, abnormal, paediatric, answer, norm, abn, nor, af, answers, diet, nom, an, teeth, fill, filled, dent, den, ans, dental, prob, probs, Ye, nots, eye, eyes, remark, opthal, psychological, psych, psy, ps, nature, motor, learning, learn) VALUES ( ? , ? , ?, ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? , ? )" , (schoolname, Standard, Name, Numbers, code, gender, DOB, age, immu, disease, Sick, Food, Meals, Junk, Water, breakfast, lunch, snacks, dinner, height, magnitude, Rate, Rates, norma, abnorma, tonsil, allergy, normal, abnormal, paediatric, answer, norm, abn, nor, af, answers, diet, nom, an, teeth, fill, filled, dent, den, ans, dental, prob, probs, Ye, nots, eye, eyes, remark, opthal, psychological, psych, psy, ps, nature, motor, learning, learn))
			  
			con.commit ()
			msg = "Record successfully added"
		
	else:
		con.rollback()
		msg = "Error in insert option"

	return render_template("index.html", msg=msg)
	con.close()


@app.route('/list')
def list():
	con = sql.connect("db_file")
	con.row_factory = sql.Row 

	cur = con.cursor()
	cur.execute("select * from students")

	rows = cur.fetchall();
	return render_template("list.html", rows=rows)




if __name__ == "__main__":
	app.run(debug = True)












