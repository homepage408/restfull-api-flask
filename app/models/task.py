from app import db, ma
from marshmallow import Schema, fields
# from app.models import user
from app.models.user import User
from datetime import datetime
import enum
from sqlalchemy.types import Enum
# from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

# status = db.Column(Enum(status_enum))
class status_enum(enum.Enum):
    approve = 1
    submit = 2
    reject = 4


class Task(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User', backref='tasks')
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    duedate = db.Column(db.DateTime, nullable=False)
    attachment = db.Column(db.String(250), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<title {self.title}>'


class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id', 'title',
                  'description', 'duedate', 'status.name')


class TaskNestedSchema(ma.ModelSchema):
    class Meta:
        model = Task


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
