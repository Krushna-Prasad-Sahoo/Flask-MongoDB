from flask import Flask,request,render_template
from pymongo import MongoClient

app = Flask("Flask with MongoDB")
db = MongoClient("mongodb://127.0.0.1:27017")

@app.route('/')
def main():
	return render_template("index.html")

@app.route('/info', methods=['POST'])
def info():
	if request.method == 'POST':
		n = request.form.get('name')
		info = [ { "Name": var } ]
		db[college][student].insert(info)
	return n

app.run(debug=True)
