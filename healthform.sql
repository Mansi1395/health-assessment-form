import sqlite3

conn = sqlite3.connect('database.db')
print "Opened database successfully";


conn.execute('CREATE TABLE students(schoolname TEXT, Standard TEXT, Name TEXT, Numbers REAL, code REAL, gender TEXT, DOB REAL, age REAL, immu TEXT, disease TEXT, Sick TEXT, Food TEXT, Meals REAL, Junk REAL, Water REAL, breakfast TEXT, lunch TEXT, snacks TEXT, dinner TEXT, height REAL, magnitude REAL, Rate REAL, Rates REAL, norma TEXT, abnorma TEXT, tonsil TEXT, allergy TEXT, normal TEXT, abnormal TEXT, paediatric TEXT, answer TEXT, norm TEXT, abn TEXT, nor TEXT, af TEXT, answers TEXT, diet TEXT, nom TEXT, an TEXT, teeth REAL, fill REAL, filled REAL, dent TEXT, den TEXT, ans TEXT, dental TEXT, prob TEXT, probs TEXT, Ye TEXT, nots TEXT, eye REAL, eyes REAL, remark TEXT, opthal TEXT, psychological TEXT, psych TEXT, psy TEXT,ps TEXT, nature TEXT, motor TEXT, learning TEXT, learn TEXT)')
print "Table created successfully"
conn.close()