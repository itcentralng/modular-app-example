from app import db
from werkzeug.security import check_password_hash as cph
from werkzeug.security import generate_password_hash as gph

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def set_password(self, password):
        self.password = gph(password)
        return True
    
    def is_valid(self, password):
        return cph(self.password, password)
    
    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def create(cls, email, password):
        user = cls(email=email)
        user.save()
        user.set_password(password)
        user.update()