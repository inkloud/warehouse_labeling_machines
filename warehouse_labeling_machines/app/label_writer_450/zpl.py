from flask import request, make_response, jsonify

import libs
from . import label_writer_450


@label_writer_450.route("/printZPL", methods=["POST", "OPTIONS"])
@libs.cors.crossdomain(origin="*")
def printZPL():
    rawZPL = request.data

    response = make_response(rawZPL, 200)
    response.mimetype = "text/plain"
    return response


@label_writer_450.route("/printZPLList", methods=["POST", "OPTIONS"])
@libs.cors.crossdomain(origin="*")
def printZPLList():
    try:
        zplList = request.get_json()

        # raise Exception("ERRORE NELLA STAMPA")
        return jsonify(zplList)
    except Exception as e:
        response = jsonify({"message": str(e)})
        response.status_code = 500
        return response
