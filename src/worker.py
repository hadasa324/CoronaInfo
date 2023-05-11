from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import WorkerModel
from schemas import WorkerSchema


blp = Blueprint("Workers", "workers", description="Operations on workers")


@blp.route("/worker/<int:worker_id>")
class Worker(MethodView):
    @blp.response(200, WorkerSchema)
    def get(self, worker_id):
        worker = WorkerModel.query.get_or_404(worker_id)
        return worker


@blp.route("/worker")
class WorkerList(MethodView):
    @blp.response(200, WorkerSchema(many=True))
    def get(self):
        return WorkerModel.query.all()

    @blp.arguments(WorkerSchema)
    @blp.response(201, WorkerSchema)
    def post(self, worker_data):
        worker = WorkerModel(**worker_data)
        try:
            db.session.add(worker)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the worker.")

        return worker