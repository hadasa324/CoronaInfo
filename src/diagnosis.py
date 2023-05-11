from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import DiagnosisModel, WorkerModel, VaccinationModel
from schemas import DiagnosesSchema

blp = Blueprint("Diagnoses", "diagnoses", description="Operations on diagnoses")


@blp.route("/diagnosis/<int:diagnosis_id>")
class Diagnosis(MethodView):
    @blp.response(200, DiagnosesSchema)
    def get(self, diagnosis_id):
        diagnosis = DiagnosisModel.query.get_or_404(diagnosis_id)
        return diagnosis




@blp.route("/diagnosis")
class DiagnosisList(MethodView):
    @blp.response(200, DiagnosesSchema(many=True))
    def get(self):
        return DiagnosisModel.query.all()

    @blp.arguments(DiagnosesSchema)
    @blp.response(201, DiagnosesSchema)
    def post(self, diagnosis_data):
        diagnosis = DiagnosisModel(**diagnosis_data)

        try:
            db.session.add(diagnosis)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the diagnosis.")

        return diagnosis