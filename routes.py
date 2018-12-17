# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Роман Гульбикс'}
    posts = [
        {
            'author': {'username': 'Oleg'},
            'body': 'Beautiful day in Saint-P!'
        },
        {
            'author': {'username': 'Mickle'},
            'body': 'The Avengers movie was so cool!'
        }, 
        {
            'author': {'username': 'Miron'},
            'body': 'Lets f***ing go!'
        }
    ]
    return render_template('index1.html', title='Home', user=user, posts=posts)