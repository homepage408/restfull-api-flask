from app import db, ma
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import enum
from sqlalchemy.types import Enum
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class role_enum(enum.Enum):
    admin = 1
    supervisor = 2
    planner = 3
    worker = 4


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(60), index=True, unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)
    # task = relationship('Task', backref='user',
    #                     cascade='all, delete', passive_deletes=True)
    # coment = relationship('Coment', backref='user',
    #                       cascade='all, delete', passive_deletes=True)

    def __repr__(self):
        return f'<User {self.name}>'

    def setPassword(self, password):
        self.password = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.password, password)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','name', 'email', 'role.name', 'created_at')


class UserForNestedSchema(ma.ModelSchema):
    class Meta:
        model = User

user_schema = UserSchema()
users_schema = UserSchema(many=True)
