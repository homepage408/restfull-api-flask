from app import db
from app.models import user
from datetime import datetime
import enum
from sqlalchemy.types import Enum
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class status_enum(enum.Enum):
    approve = 1
    submit = 2
    reject = 4


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship('User', backref='task')
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    duedate = db.Column(db.DateTime, nullable=False)
    status = db.Column(Enum(status_enum))
    attachment = db.Column(db.String(250), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<title {self.title}>'
