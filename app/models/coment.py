from app import db
from app.models import user, task
from datetime import datetime
import enum
from sqlalchemy.types import Enum
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class coment(db.Model):
    __tablename__ = 'coment'
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship('User', backref='coment')
    task_id = db.Column(db.Integer, ForeignKey('task.id', ondelete='CASCADE'))
    task = relationship('Task', backref='coment')
    comment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)
