from flask import render_template, redirect, url_for
from flask_login import current_user
from . import main

@main.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('shop.shop'))
    return render_template('home.html')


@main.route('/about')
def about():
    return render_template('about.html')
