from app import db

class level(db.Model):
    __tablename__="level"
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50),nullable=False, unique=True)

    def __repr__(self):
        return f"<level>{self.name}"