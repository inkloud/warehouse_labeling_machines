#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
'''
Per usare il log all'interno di un route devo usare:

    from web import app

    app.logger.debug('A value for debugging')
'''

from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

from app.label_writer_450 import label_writer_450
app.register_blueprint(label_writer_450, url_prefix='/label_writer_450')


if __name__ == "__main__":
    app.run(port=sys.argv[1], ssl_context=("localhost.pem", "localhost-key.pem"))





