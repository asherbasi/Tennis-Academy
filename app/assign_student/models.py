from app import db

class assign_student(db.Model):
    __tablename__="assign_student"
    id=db.Column(db.Integer, primary_key=True)
    department_id=db.Column(db.Integer, db.ForeignKey("department.id"), nullable=False)
    name=db.Column(db.String(50),nullable=False, unique=True)
    code=db.Column(db.String(10), nullable=False, unique=True)

    def __repr__(self):
        return f"<assign_student>{self.name}"