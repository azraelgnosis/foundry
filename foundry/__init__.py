import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # app.config.from_mapping(
    #     SERVER_NAME='foundry.com:5000'
    # )

    app.config['SERVER_NAME'] = "foundry.com:5000"



    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'Hello World'

    from . import dnd5
    app.register_blueprint(dnd5.bp)

    return app