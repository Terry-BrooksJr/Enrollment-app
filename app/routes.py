from app import app
from flask import  render_template

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return  render_template('index.html',login=False)

@app.route('/courses'/<int:term_year>)
@app.route('/courses')
def courses(term_year):
    course_data =[{"courseID": "1111", "title": "PHP 111", "description": "Intro to PHP", "credits": "3", "term": "Fall, Spring"}, {"courseID": "2222", "title": "Java 1", "description": "Intro to Java Programming", "credits": "4", "term": "Spring"}, {"courseID": "3333", "title": "Adv PHP 201","description": "Advanced PHP Programming", "credits": "3", "term": "Fall"}, {"courseID": "4444", "title": "Angular 1", "description": "Intro to Angular", "credits": "3", "term": "Fall, Spring"}, {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": "4", "term": "Fall"}]
    return render_template('courses.html', course_data=course_data, term_year= term_year)

@app.route('/register')
def register ():
    return render_template('register.html')


@app.route('/login')
def login():
    return render_template('login.html')
