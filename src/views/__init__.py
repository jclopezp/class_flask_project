from flask import request, json, Response, Blueprint

from ..models import BootcampModel
from ..schemas import BootcampListSchema

bootcamp_api =  Blueprint('bootcamps', __name__) # instanciamos
bootcampo_list_schema = BootcampListSchema() # incializamos el schema

@bootcamp_api.route("/", methods=['GET'])
def get_all():
    bootcamps = BootcampModel.get_all()
    data = bootcampo_list_schema.dump(bootcamps, many=True)

    return Response(
        mimetype="application/json",
        response=json.dumps({
            'data': data
        }),
        status=200
    )