from db import db


class VaccinationModel(db.Model):
    __tablename__ = "vaccinations"

    id = db.Column(db.Integer, primary_key=True)
    vaccine_date_1 = db.Column(db.Date,  nullable=True)
    vaccine_manufacturer_1 = db.Column(db.String(80),  nullable=True)
    
    vaccine_date_2 = db.Column(db.Date,  nullable=True)
    vaccine_manufacturer_2 = db.Column(db.String(80), nullable=True)
    
    vaccine_date_3 = db.Column(db.Date, nullable=True)
    vaccine_manufacturer_3 = db.Column(db.String(80),nullable=True)
    
    vaccine_date_4 = db.Column(db.Date, nullable=True)
    vaccine_manufacturer_4 = db.Column(db.String(80),  nullable=True)
    

    worker_id = db.Column(
        db.Integer, db.ForeignKey("workers.id"), unique=False, nullable=False
    )
    worker = db.relationship("WorkerModel", back_populates="vaccinations")


  