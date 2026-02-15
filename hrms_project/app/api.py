"""
REST API Routes
"""

from flask import Blueprint, request, jsonify
from datetime import date

from app import db
from app.models import Employee, Attendance

api_routes = Blueprint("api_routes", __name__)


# ---------------- HEALTH ---------------- #

@api_routes.route("/health")
def health():
    """Health Check"""

    return jsonify({"status": "running"})


# ---------------- EMPLOYEE ---------------- #

from sqlalchemy.exc import IntegrityError


@api_routes.route("/employees", methods=["POST"])
def add_employee():
    """Create Employee"""

    data = request.json

    # CHECK FIRST
    existing = Employee.query.filter_by(
        email=data["email"].lower()
    ).first()

    if existing:
        return jsonify({
            "error": "Email already exists"
        }), 409   # Conflict

    try:
        emp = Employee(
            name=data["name"],
            email=data["email"].lower(),
            designation=data.get("designation"),
            department=data.get("department"),
            address=data.get("address")
        )

        db.session.add(emp)
        db.session.commit()

        return jsonify({
            "message": "Employee Created",
            "employee": emp.to_dict()
        }), 201

    except IntegrityError:
        db.session.rollback()

        return jsonify({
            "error": "Duplicate email"
        }), 409

    except Exception as e:
        db.session.rollback()

        return jsonify({
            "error": "Server error"
        }), 500


# ---------------- ATTENDANCE ---------------- #

@api_routes.route("/attendance", methods=["POST"])
def mark_attendance():
    """Mark Attendance"""

    data = request.json

    att = Attendance(
        employee_id=data["employee_id"],
        date=date.today(),
        in_time=data.get("in_time"),
        out_time=data.get("out_time")
    )

    db.session.add(att)
    db.session.commit()

    return jsonify({
        "message": "Attendance Marked"
    })


@api_routes.route("/attendance/<int:emp_id>")
def get_attendance(emp_id):
    """Get Attendance"""

    data = Attendance.query.filter_by(
        employee_id=emp_id
    ).all()

    return jsonify([
        a.to_dict() for a in data
    ])
