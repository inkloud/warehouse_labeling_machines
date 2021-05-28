from flask import request

import libs
from . import label_writer_450


@label_writer_450.route("/printZPL", methods=["POST", "OPTIONS"])
@libs.cors.crossdomain(origin="*")
def printZPL():
    print(request.data)
    return "okkkkk"
