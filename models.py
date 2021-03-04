from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from run import db
from slugify import slugify

class User(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.String(80), nullable=False)
    def __repr__(self):
        return f'<User {self.email}>'
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    @staticmethod
    def get_by_mensaje(mensaje):
        return User.query.filter_by(mensaje=mensaje).first()
