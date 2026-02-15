"""
Database Models
"""

from datetime import datetime, date
from app import db


class Employee(db.Model):
    """Employee Table"""

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    designation = db.Column(db.String(100))

    department = db.Column(db.String(100))

    address = db.Column(db.Text)

    date_of_joining = db.Column(db.Date, default=date.today)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    attendances = db.relationship(
        "Attendance",
        backref="employee",
        cascade="all, delete"
    )

    def to_dict(self):
        """Serialize Employee"""

        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "designation": self.designation,
            "department": self.department,
            "address": self.address,
            "date_of_joining": str(self.date_of_joining)
        }


class Attendance(db.Model):
    """Attendance Table"""

    __tablename__ = "attendance"

    id = db.Column(db.Integer, primary_key=True)

    employee_id = db.Column(
        db.Integer,
        db.ForeignKey("employees.id"),
        nullable=False
    )

    date = db.Column(db.Date, default=date.today)

    in_time = db.Column(db.String(10))

    out_time = db.Column(db.String(10))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Serialize Attendance"""

        return {
            "date": str(self.date),
            "in_time": self.in_time,
            "out_time": self.out_time
        }
