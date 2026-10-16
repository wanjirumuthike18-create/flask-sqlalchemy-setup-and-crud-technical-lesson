from flask import Flask
from flask_migrate import Migrate
from models import db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)  # handles database version changes
db.init_app(app)            # connects db to this app

if __name__ == '__main__':
    app.run(port=5555, debug=True)