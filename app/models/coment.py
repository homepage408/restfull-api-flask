from app import db, ma
from marshmallow import Schema, fields
from app.models.user import User
from app.models.task import Task
from datetime import datetime
import enum
from sqlalchemy.types import Enum
from sqlalchemy import ForeignKey


class coment(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = db.relationship('User', backref='coments')
    task_id = db.Column(db.Integer, ForeignKey('task.id', ondelete='CASCADE'))
    task = db.relationship('Task', backref='coments')
    comment = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<nomor id {self.id}>'


class CommentSchema(ma.Schema):
    class Meta:
        fields = ("id", "user_id", "task_id", "comment", "created_at")


class CommentForNestedSchema(ma.ModelSchema):
    class Meta:
        model = coment


comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True)

# comment_nested_schema = CommentForNestedSchema()
# comments_nested_schema = CommentForNestedSchema(many=True)
