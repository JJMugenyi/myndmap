from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/login')
def login():
    return render_template('login.html')

@views.route('/signup')
def signup():
    return render_template('signup.html')

@views.route('/pricing')
def pricing():
    return render_template('pricing.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/forgot')
def forgot():
    return render_template('forgot_pass.html')

@views.route('/privacy')
def privacy():
    return render_template('privpol.html')

@views.route('/onboard')
def onboard():
    return render_template('onboard1.html')

@views.route('/onboard2')
def onboard2():
    return render_template('onboard2.html')

@views.route('/onboard3')
def onboard3():
    return render_template('onboard3.html')

@views.route('/adhd_ai')
def adhd_ai():
    return render_template('adhd_ai.html')

@views.route('/adhd_ai_2')
def adhd_ai_2():
    return render_template('adhd_ai_2.html')

@views.route('/results')
def results():
    return render_template('results.html')


