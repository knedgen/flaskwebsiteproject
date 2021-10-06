from flask import render_template,request,Blueprint
from portfoliowebsite.models import ProjectPost

core = Blueprint('core',__name__)

@core.route('/')
def index():
    return render_template('index.html')

@core.route('/contact')
def contact():
    return render_template('contact.html')

@core.route('/projects')
def projects():
    projects = ProjectPost.query.all()
    return render_template('projects.html', projects=projects)

@core.route('/about')
def about():
    return render_template('about.html')

@core.route('/udemy_classes')
def udemy():
    return render_template('udemy.html')
