from db import db


class DiagnosisModel(db.Model):
    __tablename__ = "diagnoses"

    id = db.Column(db.Integer, primary_key=True)
    positive_result_date = db.Column(db.Date,  nullable=True)
    recovery_date = db.Column(db.Date,  nullable=True)
    worker_id = db.Column(db.Integer, db.ForeignKey("workers.id"), nullable=False)

    worker = db.relationship("WorkerModel", back_populates="diagnoses")

     
  