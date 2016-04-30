from app import db
from datetime import datetime


class Todo(db.Document):
    content = db.StringField(require=True, max_length=20)
    create_at = db.DateTimeField(default=datetime.now())
    update_at = db.DateTimeField(default=datetime.now())
    status = db.IntField(defult=0)
