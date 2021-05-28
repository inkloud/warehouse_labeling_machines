from flask import request, make_response

import libs
from . import label_writer_450


@label_writer_450.route("/printZPL", methods=["POST", "OPTIONS"])
@libs.cors.crossdomain(origin="*")
def printZPL():
    rawZPL = request.data

    response = make_response(rawZPL, 200)
    response.mimetype = "text/plain"
    return response
