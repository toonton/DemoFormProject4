"""
Routes and views for the flask application.
"""

from DemoFormProject import app
from datetime import datetime
from flask import render_template
from DemoFormProject.Models.LocalDatabaseRoutines import create_LocalDatabaseServiceRoutines

from datetime import datetime
from flask import render_template, redirect, request

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import json 
import requests

import io
import base64

from os import path

from flask   import Flask, render_template, flash, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms import TextField, TextAreaField, SubmitField, SelectField, DateField
from wtforms import ValidationError


from DemoFormProject.Models.QueryFormStructure import QueryFormStructure 
from DemoFormProject.Models.QueryFormStructure import LoginFormStructure 
from DemoFormProject.Models.QueryFormStructure import UserRegistrationFormStructure 

###from DemoFormProject.Models.LocalDatabaseRoutines import IsUserExist, IsLoginGood, AddNewUser 

db_Functions = create_LocalDatabaseServiceRoutines() 


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='matan home page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/About')
def About():
    """Renders the about page."""
    return render_template(
        'About.html',
        title='About my website',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/Data')
def Data():
    """Renders the about page."""
    return render_template(
        'Data.html',
        title='Data',
        year=datetime.now().year,
        message='My data is here.'
        
       
    )



@app.route('/Datatwo')
def Datatwo():

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\Global.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')


    """Renders the contact page."""
    return render_template(
        'Datatwo.html',
        title='Global warming Database',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='aaaa'
    )



@app.route('/Dataone')
def Dataone():

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\Global.csv'))
    raw_data_table = df.to_html(classes = 'table table-hover')


    """Renders the contact page."""
    return render_template(
        'Dataone.html',
        title='Global warming Database',
        raw_data_table = raw_data_table,
        year=datetime.now().year,
        message='gamer'
    )



@app.route('/Album')
def Album():
    """Renders the about page."""
    return render_template(
        'PictureAlbum.html',
        title='Pictures',
        year=datetime.now().year,
        message='Welcome to my picture album'
    )


@app.route('/Query', methods=['GET', 'POST'])
def Query():

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\Pokemon.csv'))
    print("im in query")
    Name = None
    Country = ''

    df = pd.read_csv(path.join(path.dirname(__file__), 'static\\Data\\Pokemon.csv'))
    Pokemon_choise = list(set(df['Name']))
    m = list(zip(Pokemon_choise , Pokemon_choise))
    form1.Pokemon.choices = m 
    form2.Pokemon.choices = m




    
    

    form = QueryFormStructure(request.form)
     
    raw_data_table = df.to_html(classes = 'table table-hover')

    return render_template('Query.html', 
           
            raw_data_table = raw_data_table,
            title='Query by the user',
            year=datetime.now().year,
            message='This page will use the web forms to get user input'
        )

# -------------------------------------------------------
# Register new user page
# -------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
	form = UserRegistrationFormStructure(request.form)

	if (request.method == 'POST'):
		if form.validate():
			if (not db_Functions.IsUserExist(form.username.data)):
				db_Functions.AddNewUser(form)
				db_table = ""

				flash('Welcome '+ form.FirstName.data + " " + form.LastName.data + "!")
			else:
				flash('Error: User ' + form.username.data + ' already exists.')
				form = UserRegistrationFormStructure(request.form)
		else:
			flash('Some fields are invalid.')

	return render_template(
		'register.html', 
		form=form, 
		title=mutualtitle + ' - Register',
		year=datetime.now().year,
		repository_name='Pandas',
		)

# -------------------------------------------------------
# Login page
# This page is the filter before the data analysis
# -------------------------------------------------------
@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginFormStructure(request.form)

    if (request.method == 'POST' and form.validate()):
        if (db_Functions.IsLoginGood(form.username.data, form.password.data)):
            flash('Login approved!')
            #return redirect('<were to go if login is good!')
        else:
            flash('Error in - Username and/or password')
   
    return render_template(
        'login.html', 
        form=form, 
        title='Login to data analysis',
        year=datetime.now().year,
        repository_name='Pandas',
        )


