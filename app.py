from flask import Flask, render_template, redirect, request, url_for, flash, session
import os



app = Flask(__name__)
app.secret_key = "faketutorialsecretsoinsecuremuchwow"




@app.route("/")
def index():
	return render_template("index.html")














if __name__ == "__main__":
	app.run(debug = True)