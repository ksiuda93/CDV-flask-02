from flask import Flask
from flask_migrate import Migrate
from models.User import db, ma
from routes.user import user_bp

URL_PREFIX = "/api/v1"

app = Flask(__name__)
app.config.update(
    ENV="development",
    DEBUG=True,
    SQLALCHEMY_DATABASE_URI="sqlite:///app.db",
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SQLALCHEMY_ECHO=True,
)

db.init_app(app)
ma.init_app(app)
migrate = Migrate(app,db)

app.register_blueprint(user_bp, url_prefix=URL_PREFIX)
if __name__ == "__main__":
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run()
