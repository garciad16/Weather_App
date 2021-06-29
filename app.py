from flask import Flask, redirect, url_for, render_template, request, session, json, jsonify
import requests
import MySQLdb
import MySQLdb.cursors
import re

app = Flask(__name__, static_url_path='')
app.secret_key = 'bY\x7fl\x8c\xde]\xbf\x8f\x87\xcd\x843\xfa\xb1J['
#app id = 8cf7f3daab7b3b9ec93948d0b1c6e5f6

db = MySQLdb.connect(host="dursley.socs.uoguelph.ca",
		user="garciad",
		password="1022106",
		db="garciad")

@app.route('/', methods=['GET', 'POST'])
def home():
	city = request.form.get('city')
	cursor = db.cursor();

	cursor.execute("INSERT IGNORE INTO City(city) VALUES (%s)", [city])
	db.commit();
	
	query = ("SELECT * FROM City WHERE City IS NOT NULL");
	cursor.execute(query);
	records = cursor.fetchall()
	
	weather_data = []
	
	for city_name in records:
		city_name = ''.join(city_name)
		url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8cf7f3daab7b3b9ec93948d0b1c6e5f6'
		r = requests.get(url.format(city_name)).json()
		if city_name and not city_name.isspace():
			#print(city_name)
			weather = {
				'city': city_name,
				'temperature': r['main']['temp'],
				'description': r['weather'][0]['description'],
				'icon': r['weather'][0]['icon']
			}
			
			weather_data.append(weather)

	
	#print(weather);
	return render_template('index.html', weather_data=weather_data)
	
@app.route("/login", methods=["POST", "GET","PUT"])
def login():
	if request.method == "POST":
		userN = request.form["username"]
		passW = request.form['password'];
		cursor = db.cursor();
		session['logged_in'] = True;
		msg = cursor.execute("SELECT username FROM MyUsers WHERE username=%s AND password=%s", (userN,passW));
		if (msg>0):
			session["user"] = userN
			db.commit();
			return redirect(url_for("user"))
		elif (msg == 0):
			msg2 = cursor.execute("SELECT username FROM MyUsers WHERE username=%s", [userN]);
			if (msg2 > 0):
				print('wrong password')
				return render_template("index.html")
			elif (msg2 == 0):
				session["user"] = userN
				cursor.execute("INSERT INTO MyUsers(username, password) VALUES (%s, %s)", (userN, passW))
				db.commit();
				return redirect(url_for("user"))
	elif request.method == 'PUT':
		userN = request.form["username"]
		passW = request.form['password'];
		session["user"] = userN
		session['logged_in'] = True;
		cursor = db.cursor();
		cursor.execute("UPDATE MyUsers SET password=%s WHERE username=%s", (passW, userN));
		db.commit();
		return redirect(url_for("login"))
	else:
		if "user" in session:
			return redirect(url_for("user"))
		return render_template("index.html")

@app.route('/login', methods=['DELETE'])
def deleteUser():
	cursor = db.cursor();
	cursor.execute("DELETE FROM MyUsers");
	db.commit();
	return redirect(url_for("login"))
		
@app.route("/user")
def user():
	if "user" in session:
		user = session["user"]
		return render_template("index.html")
	else:
		return redirect(url_for("login"))

@app.route("/logout")
def logout():
	session['logged_in'] = False;
	session.pop("user", None)
	return redirect(url_for("login"))

@app.route("/delete/<name>")
def delete_city(name):
	print(name);
	cursor = db.cursor();
	cursor.execute("DELETE FROM City WHERE city=%s", [name]);
	db.commit();
	return redirect(url_for('home'))

if __name__ == "__main__":
	app.run(debug=True)
	
