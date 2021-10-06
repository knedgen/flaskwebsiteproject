from flask import render_template,url_for,request,redirect,Blueprint
from flask_login import current_user,login_required
from portfoliowebsite import db
from portfoliowebsite.models import ProjectPost
from portfoliowebsite.projects.forms import ProjectPostForm
from portfoliowebsite.projects.picture_handler import add_picture

projects = Blueprint('projects',__name__)

#post a project
@projects.route('/add',methods=['GET','POST'])
@login_required
def add_project():

    form = ProjectPostForm()

    if form.validate_on_submit():

            project_post = ProjectPost(title=form.title.data,
                                    description= form.description.data,
                                    link = form.link.data)

            db.session.add(project_post)
            db.session.commit()
            return redirect(url_for('core.projects'))

    return render_template('add_project.html', form=form)




#update project post
@projects.route('/<int:project_id>/update', methods=['GET','POST'])
@login_required
def update(project_id):
    project_post = ProjectPost.query.get_or_404(project_id)

    if current_user.is_authenticated == False:
        abort()

    form = ProjectPostForm()

    if form.validate_on_submit():

            project_post.title = form.title.data
            project_post.description= form.description.data
            project_post.link = form.link.data
            db.session.commit()
            return redirect(url_for('core.projects', project_id=project_post.id))

    elif request.method == 'GET':

        form.title.data = project_post.title
        form.description.data = project_post.description
        form.link.data = project_post.link

    return render_template('add_project.html',form=form)

#view a projects page
@projects.route('/<int:project_id>')
def project_page(project_id):
    project_page = ProjectPost.query.get_or_404(project_id)
    return render_template('project_page.html',title=project_page.title,
                            description=project_page.description,
                            link=project_page.link, id = project_page.id,
                            post = project_page)

#delete a project
@projects.route('/<int:project_id>/deleteproject',methods=['GET','POST'])
@login_required
def delete_post(project_id):
    project_post = ProjectPost.query.get_or_404(project_id)
    if current_user.is_authenticated == False:
        abort()
    db.session.delete(project_post)
    db.session.commit()
    return redirect(url_for('core.projects'))
