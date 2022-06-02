from settings import *
import datetime
import json

db = SQLAlchemy(app)

class Hospital(db.Model):
    __tablename__ = 'hospital'
    id = db.Column(db.Integer, primary_key = True)
    patientName = db.Column(db.String(80), nullable = False)
    doctorName = db.Column(db.String(80), nullable = False)
    appointmentDate = db.Column(db.DateTime, nullable=False, default = datetime.datetime.utcnow)

    def json(self):
        return {'id': self.id,
        'patientName':self.patientName,
        'doctorName':self.doctorName,
        'appointmentDate': self.appointmentDate
        }

    def add_appointment(_patientName, _doctorName, _appointmentDate):
        new_appointment = Hospital(patientName = _patientName, doctorName = _doctorName, appointmentDate = _appointmentDate)
        db.session.add(new_appointment)
        db.session.commit()

    def get_all_appointment():
        return [Hospital.json(hospital) for hospital in Hospital.query.all()]

    def get_appointment(_id):
        return [Hospital.json(Hospital.query.filter_by(id=_id).first())]

    def update_appointment(_id, _patientName, _doctorName, _appointmentDate):
        appointment_to_update = Hospital.query.filter_by(id=_id).first()
        appointment_to_update.patientName = _patientName
        appointment_to_update.doctorName = _doctorName
        appointment_to_update.appointmentDate = _appointmentDate
        db.session.commit()

    def delete_appointment(_id):
        Hospital.query.filter_by(id=_id).delete()
        db.session.commit()