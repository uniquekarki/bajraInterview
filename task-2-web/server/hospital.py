from settings import *
import datetime
import json

db = SQLAlchemy(app)

class Hospital(db.Model):
    __tablename__ = 'hospital'
    id = db.Column(db.Integer, primary_key = True)
    patientName = db.Column(db.String(80), nullable = False)
    doctorName = db.Column(db.String(80), nullable = False)
    appointmentDate = db.Column(db.DateTime, nullable=False,
        default = datetime.datetime.utcnow)

    def json(self):
        return {'id': self.id,
        'patientName':self.patientName,
        'doctorName':self.doctorName,
        'appointmentDate': self.appointmentDate
        }

    def add_appointment(self, patientName, doctorName, appointmentDate):
        new_appointment = Hospital(patientName = patientName, doctorName = doctorName, appointmentDate = appointmentDate)
        db.session.add(new_appointment)
        db.session.commit()

    def get_all_appointment(self):
        return [Hospital.json(hospital) for hospital in Hospital.query.all()]

    def get_appointment(self, id):
        return [Hospital.json(Hospital.query.filter_by(id=id).first())]

    def update_appointment(self, id, patientName, doctorName, appointmentDate):
        appointment_to_update = Hospital.query.filter_by(id=id).first()
        appointment_to_update.patientName = patientName
        appointment_to_update.doctorName = doctorName
        appointment_to_update.appointmentDate = appointmentDate
        db.session.commit()

    def delete_appointment(self, id):
        Hospital.query.filter_by(id=id).delete()
        db.session.commit()