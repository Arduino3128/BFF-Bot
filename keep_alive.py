from flask import Flask, render_template, redirect
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
	return redirect("https://arduino3128.github.io/BFF-Bot/", code=200)
def run():
	app.run(host='0.0.0.0', port=8080)
def keep_alive():
	t=Thread(target=run)
	t.start()