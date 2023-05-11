from db import db


class WorkerModel(db.Model):
    __tablename__ = "workers"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), unique=True, nullable=False)
    last_name = db.Column(db.String(50), unique=True, nullable=False)
    city = db.Column(db.String(80), unique=True, nullable=False)
    street = db.Column(db.String(80), unique=True, nullable=False)
    address_number = db.Column(db.String(10), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, unique=True, nullable=False)
    telephone = db.Column(db.String(20), unique=True, nullable=False)
    mobile_phone = db.Column(db.String(20), unique=True, nullable=False)
    vaccinations = db.relationship("VaccinationModel", back_populates="worker", lazy="dynamic")
    diagnoses = db.relationship("DiagnosisModel", back_populates="worker", lazy="dynamic")


