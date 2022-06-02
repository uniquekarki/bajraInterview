from settings import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager
from datetime import datetime
import json

db = SQLAlchemy(app)

login = LoginManager()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String())
 
    def set_password(self,_password):
        self.password = generate_password_hash(_password)
     
    def check_password(self,_password):
        return check_password_hash(self.password, _password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Hospital(db.Model):
    __tablename__ = 'hospital'
    id = db.Column(db.Integer, primary_key = True)
    patientName = db.Column(db.String(80), nullable = False)
    doctorName = db.Column(db.String(80), nullable = False)
    appointmentDate = db.Column(db.DateTime, nullable=False)

    def json(self):
        return {'id': self.id,
        'patientName':self.patientName,
        'doctorName':self.doctorName,
        'appointmentDate': self.appointmentDate
        }

    def add_appointment(_patientName, _doctorName, _appointmentDate):
        dateTime = datetime.strptime(_appointmentDate, '%d/%m/%y %H:%M')
        print(dateTime)
        new_appointment = Hospital(patientName = _patientName, doctorName = _doctorName, appointmentDate = dateTime)
        db.session.add(new_appointment)
        db.session.commit()

    def get_all_appointment():
        return [Hospital.json(hospital) for hospital in Hospital.query.all()]

    def get_appointment(_id):
        return [Hospital.json(Hospital.query.filter_by(id=_id).first())]

    def update_appointment(_id, _patientName, _doctorName, _appointmentDate):
        dateTime = datetime.strptime(_appointmentDate, '%d/%m/%y %H:%M')
        appointment_to_update = Hospital.query.filter_by(id=_id).first()
        appointment_to_update.patientName = _patientName
        appointment_to_update.doctorName = _doctorName
        appointment_to_update.appointmentDate = dateTime
        db.session.commit()

    def delete_appointment(_id):
        Hospital.query.filter_by(id=_id).delete()
        db.session.commit()