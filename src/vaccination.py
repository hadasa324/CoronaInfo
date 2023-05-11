from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import VaccinationModel
from schemas import VaccinationSchema

blp = Blueprint("Vaccinations", "vaccinations", description="Operations on vaccinations")


@blp.route("/vaccination/<string:vaccination_id>")
class Vaccination(MethodView):
    @blp.response(200, VaccinationSchema)
    def get(self, vaccination_id):
        vaccination = VaccinationModel.query.get_or_404(vaccination_id)
        return vaccination




@blp.route("/vaccination")
class VaccinationList(MethodView):
    @blp.response(200, VaccinationSchema(many=True))
    def get(self):
        return VaccinationModel.query.all()

    @blp.arguments(VaccinationSchema)
    @blp.response(201, VaccinationSchema)
    def post(self, vaccination_data):
        vaccination = VaccinationModel(**vaccination_data)
        try:
            db.session.add(vaccination)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the vaccination.")

        return vaccination