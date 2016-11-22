from flask import render_template, flash, redirect
from app import app
#from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html', title='Home', active='index')

@app.route('/get-pass', methods=['GET'])
def get_pass():
    pass