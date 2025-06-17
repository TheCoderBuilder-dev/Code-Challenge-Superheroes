# import the basic Flask tools we need
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow  # I know we didnt read this but i read that it is used to serialize models into JSON


from superheroes_api import create_app

app = create_app()

app.config.from_object('config.Config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

from routes import *
if __name__ == '__main__':
    app.run(port=5555, debug=True)
