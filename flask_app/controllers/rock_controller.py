from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.rock_model import Rock


@app.route('/')
def display_homepage():
    return render_template("homepage.html", rocks = Rock.get_all())

@app.route('/log')
def display_form():
    return render_template("rock_log.html")

@app.route('/rock/create', methods=['POST'])
def create_rock():
    print(request.form)
    Rock.create(request.form)
    return redirect('/')
