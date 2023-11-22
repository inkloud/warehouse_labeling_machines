#!/usr/bin/python
# -*- coding: utf-8 -*-

import flask
import json
import libs
import os
from base64 import b64decode
import re
from PyPDF2 import PdfFileMerger
from subprocess import run

from . import label_writer_450
import time


def createFile(pdfs, filename):
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)

    merger.write(filename)
    merger.close()


def printFile(filename, printer_name=None):
    print("---- START PRINTING ----")
    args = [".\PDFtoPrinter.exe", filename]
    if printer_name is not None:
        args.append(printer_name)
    return run(args)


@label_writer_450.route("/", methods=["GET", "OPTIONS"])
@libs.cors.crossdomain(origin="*")
def index():
    return "warehouse labeling pinter service active (with printer name)!!!"


@label_writer_450.route("/printPDF", methods=["POST", "PUT", "OPTIONS"])
@libs.cors.crossdomain(origin="*")
def printPDF():

    ## save file
    print("inizia procedura di stampa")
    data = flask.request.get_json()
    printer = data.get("printer", None)
    labels = data["label"]
    orderId = data["orderId"]
    startingBox = None
    if "startingBox" in data:
        startingBox = data["startingBox"]
    stream = "stream"
    if "stream" in data:
        stream = data["stream"]
    list_filename = []

    ### save files
    for l in range(0, len(labels)):
        print("Salva etichetta")
        b64 = labels[l][stream]
        binary = b64decode(b64, validate=True)
        boxToPrint = l
        if startingBox is not None:
            boxToPrint = boxToPrint + startingBox
        filename = "{}parcel{}.pdf".format(orderId, boxToPrint)
        list_filename.append(filename)
        f = open(filename, "wb")
        f.write(binary)
        f.close()

    ### merge pdf

    completefile = "{}.pdf".format(orderId)
    createFile(list_filename, completefile)
    res = printFile(completefile, printer)
    return "ok"


@label_writer_450.route("/reprintPDF", methods=["POST", "PUT", "OPTIONS"])
@libs.cors.crossdomain(origin="*")
def reprintPDF():
    data = flask.request.get_json()
    printer = data.get("printer", None)
    orderId = data["orderId"]

    rootdir = "."
    regex = re.compile("{}parcel\d.pdf".format(orderId))
    toPrint = []
    for root, dirs, files in os.walk(rootdir):
        for file in files:
            if regex.match(file):
                toPrint.append(file)
                print(file)

    if len(toPrint) == 0:
        return "No label found", 404
    else:
        completefile = "{}.pdf".format(orderId)
        createFile(toPrint, completefile)
        printFile(completefile, printer)
        return "ok", 200
