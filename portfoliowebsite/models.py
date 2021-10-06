from portfoliowebsite import db,login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_admin(admin_id):
    return Admin.query.get(admin_id)

class Admin(db.Model,UserMixin):

    __tablename__ = 'admin'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(),unique=True,index=True)
    password_hash = db.Column(db.String)

    def __init__(self,username,password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f"Admin name {self.username}"

class ProjectPost(db.Model):

    __tablename__ = 'projects'

    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    title = db.Column(db.String,nullable=False)
    description = db.Column(db.Text,nullable=False)
    link = db.Column(db.Text,nullable=True)

    def __init__(self,title,description,link):
        self.title = title
        self.description = description
        self.link = link

    def __repr__(self):
        return f"Post id {self.id} -- Date {self.date} -- {self.title}"
