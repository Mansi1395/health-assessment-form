import os
import sqlite3
from sqlite3 import Error

from flask import Flask, g, flash, redirect, render_template, request, url_for

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


@app.route('/pygalexample/')
def pygalexample():
    graph = pygal.Pie()
    graph.title = 'PERCENTAGE OF STUDENTS WHO REQUIRE FURTHER CONSULTATION'
    graph.add('Yes', 25)
    graph.add('No', 75)
    graph_data = graph.render_data_uri()
    return render_template('graphing.html', graph_data=graph_data)


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
        immu = request.form['immu']
        disease = request.form['disease']
        sick = request.form['sick']
        food = request.form['food']
        meals = request.form['meals']
        junk = request.form['junk']
        water = request.form['water']
        breakfast = request.form['breakfast']
        lunch = request.form['lunch']
        snacks = request.form['snacks']
        dinner = request.form['dinner']
        height = request.form['height']
        magnitude = request.form['magnitude']
        rate = request.form['rate']
        rates = request.form['rates']
        norma = request.form['norma']
        abnorma = request.form['abnorma']
        tonsil = request.form['tonsil']
        allergy = request.form['allergy']
        # times = request.form['times']
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
        ye = request.form['ye'] 
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
    con = sqlite3.connect("db_file")
    con.row_factory = sqlite3.Row 

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)




if __name__ == "__main__":
    app.run(debug = True)
