###################### Template Docs #######################
# Author: Michael Valdron                                  #
# License: MIT License                                     #
#                                                          #
# This template does not include the database source, this #
# can be added to the procedure below.                     #
############################################################

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # register blueprints
    # app.register_blueprint(..)

    return app
