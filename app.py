from flask import Flask
from flask_migrate import Migrate
from models.User import db, ma, bc
from routes.user import user_bp
from flask_jwt import JWT
from services.jwt_handler import authenticate, identity

URL_PREFIX = "/api/v1"

app = Flask(__name__)
app.config.update(
    ENV="development",
    DEBUG=True,
    SECRET_KEY="cdvSecret1231231515161&2311211",
    JWT_AUTH_HEADER_PREFIX="CDV",
    SQLALCHEMY_DATABASE_URI="mysql://cdv-app:tajneHaslo123*@localhost/cdv_app",
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SQLALCHEMY_ECHO=True,
)

db.init_app(app)
ma.init_app(app)
bc.init_app(app)
jwt = JWT(app, authenticate, identity)
migrate = Migrate(app, db)

app.register_blueprint(user_bp, url_prefix=URL_PREFIX)
if __name__ == "__main__":
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run()
