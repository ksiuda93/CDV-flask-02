from . import db, exc, ma, bc


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), unique=True, nullable=False)
    email = db.Column(db.String(256), nullable=False)
    password = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(256), nullable=True)

    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.password = bc.generate_password_hash(password)
        self.role = role

    def __repr__(self):
        return f"<{__name__} {self.id} {self.username}>"

    def add_user(self):
        try:
            db.session.add(self)
            db.session.commit()
            db.session.close()
            return True
        except exc.SQLAlchemyError as db_error:
            print(db_error)
            db.session.rollback()
            return False

    def delete_user(self):
        try:
            db.session.delete(self)
            db.session.commit()
            db.session.close()
            return True
        except exc.SQLAlchemyError as db_error:
            print(db_error)
            db.session.rollback()
            return False


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User