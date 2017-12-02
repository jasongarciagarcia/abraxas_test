import os
from flask import Flask, request

app = Flask(__name__)
i   = 0

@app.route("/")
def index():
	return "index"

@app.route('/increaseVisitor',methods=['POST'])
def increaseVisitor():
	global i
	i += 1
	return "Thanks for visiting us!"

@app.route('/viewVisitor')
def viewVisitor():
	global i
	return 'Number of visitors: ' + str(i)

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
