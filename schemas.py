from marshmallow import Schema , fields

class PlainVaccinationSchema(Schema):
    id = fields.Int(dump_only=True)
    vaccine_date_1 = fields.Date()
    vaccine_manufacturer_1 = fields.Str()
    
    vaccine_date_2 = fields.Date()
    vaccine_manufacturer_2 = fields.Str()
    
    vaccine_date_3 = fields.Date()
    vaccine_manufacturer_3 = fields.Str()
    
    vaccine_date_4 = fields.Date()
    vaccine_manufacturer_4 = fields.Str()

class PlainWorkerSchema(Schema):
    id = fields.Int(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    city = fields.Str(required=True)
    street = fields.Str(required=True)
    address_number = fields.Str(required=True)
    date_of_birth = fields.Date(required=True)
    telephone = fields.Str(required=True)
    mobile_phone = fields.Str(required=True)

class PlainDiagnosesSchema(Schema):
    id = fields.Int(dump_only=True)
    positive_result_date = fields.Date()
    recovery_date = fields.Date()

class VaccinationSchema(PlainVaccinationSchema):
    worker_id = fields.Int(required=True, load_only=True)
    worker = fields.Nested(PlainWorkerSchema(), dump_only=True)

class WorkerSchema(PlainWorkerSchema):
    vaccinations = fields.List(fields.Nested(PlainVaccinationSchema()), dump_only=True)
    diagnoses = fields.List(fields.Nested(PlainDiagnosesSchema()), dump_only=True)

class DiagnosesSchema(PlainDiagnosesSchema):
    worker_id = fields.Int( load_only=True)
    worker = fields.Nested(PlainWorkerSchema(), dump_only=True)