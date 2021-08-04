from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/oscon')
def oscon():
  return render_template("oscon.html")

@app.route('/networks')
def networks():
  return render_template("networks.html")

@app.route('/poynt')
def poynt():
  return render_template("poynt.html")

@app.route('/node')
def node():
  return render_template("node.html")