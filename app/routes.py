from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

# Decorators provide URLS for following index function.
@app.route('/')
@app.route('/index')
def index():
    # Declare dummy data for username/posts as no user system in place.
    user = {"username" : "Harry"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Harry'},
            'body': "I'm trying to learn Flask rn!"
        }
    ]

    # Return a render_template() function that creates the full page with vars
    # as arguments to the result.
    return render_template('index.html', user=user, title="Home", posts=posts)

# Making my own route for an 'about' page that utilises a template made like earlier.
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Function takes decorator for login URL and HTTP methods and creates login page.
    """
    form = LoginForm() # Create new login form using LoginForm() function.

    # If user clicks submit button.
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data)) # Return to
        return redirect('/index')
    return render_template('login.html', title='Sign in', form=form)
