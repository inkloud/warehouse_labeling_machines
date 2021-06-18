import os, tempfile

from flask import request, make_response, jsonify

import libs
from . import label_writer_450


def saveZPL(body):
    fd, path = tempfile.mkstemp()
    with os.fdopen(fd, "w") as tmp:
        tmp.write(body)
    return path


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
    """
    notepad /pt "zpl.txt" "BARTZEBRA"
    """
    try:
        zplList = request.get_json()
        for zpl in zplList:
            fName = saveZPL(zpl["zpl"])
            os.system(f'notepad /pt "{fName}" "BARTZEBRA"')

        # raise Exception("ERRORE NELLA STAMPA")
        return jsonify(zplList)
    except Exception as e:
        response = jsonify({"message": str(e)})
        response.status_code = 500
        return response
