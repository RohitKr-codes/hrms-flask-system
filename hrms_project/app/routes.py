"""
Frontend Routes
"""

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from sqlalchemy import func
from datetime import date, datetime

from app.models import Employee, Attendance
from app import db


# ================= BLUEPRINT =================

main_routes = Blueprint("main_routes", __name__)


# ================= DASHBOARD =================

@main_routes.route("/")
def home():

    total = Employee.query.count()

    today = date.today()

    present = Attendance.query.filter_by(
        date=today
    ).count()

    return render_template(
        "home.html",
        total=total,
        present=present
    )


# ================= EMPLOYEES =================

@main_routes.route("/employees", methods=["GET", "POST"])
def employees():

    if request.method == "POST":

        name = request.form["name"].strip()
        email = request.form["email"].strip().lower()
        department = request.form["department"].strip()
        designation = request.form["designation"].strip()

        existing = Employee.query.filter_by(email=email).first()

        if existing:
            flash("❌ Email already exists!", "danger")
            return redirect(url_for("main_routes.employees"))

        try:

            emp = Employee(
                name=name,
                email=email,
                department=department,
                designation=designation
            )

            db.session.add(emp)
            db.session.commit()

            flash("✅ Employee Added Successfully", "success")

        except Exception:

            db.session.rollback()
            flash("⚠️ Server Error", "danger")

        return redirect(url_for("main_routes.employees"))

    data = Employee.query.order_by(
        Employee.created_at.desc()
    ).all()

    return render_template(
        "employees.html",
        employees=data
    )


# ================= ATTENDANCE =================

@main_routes.route("/attendance", methods=["GET", "POST"])
def attendance():

    employees = Employee.query.all()

    today = date.today()

    if request.method == "POST":

        emp_id = request.form["employee_id"]
        action = request.form["action"]

        record = Attendance.query.filter_by(
            employee_id=emp_id,
            date=today
        ).first()

        # ---------- CHECK IN ----------

        if action == "in":

            if record and record.in_time:
                flash("❌ Already Checked In Today", "danger")
                return redirect(url_for("main_routes.attendance"))

            if not record:
                record = Attendance(
                    employee_id=emp_id,
                    date=today
                )

                db.session.add(record)

            record.in_time = datetime.now().strftime("%H:%M")

            db.session.commit()

            flash("✅ Check-In Successful", "success")

        # ---------- CHECK OUT ----------

        elif action == "out":

            if not record or not record.in_time:
                flash("❌ Check-In First", "danger")
                return redirect(url_for("main_routes.attendance"))

            if record.out_time:
                flash("❌ Already Checked Out", "danger")
                return redirect(url_for("main_routes.attendance"))

            record.out_time = datetime.now().strftime("%H:%M")

            db.session.commit()

            flash("✅ Check-Out Successful", "success")

        return redirect(url_for("main_routes.attendance"))

    today_records = Attendance.query.filter_by(
        date=today
    ).all()

    return render_template(
        "attendance.html",
        employees=employees,
        records=today_records
    )


# ================= EMPLOYEE DETAILS =================

@main_routes.route("/employees/<int:emp_id>")
def employee_detail(emp_id):

    emp = Employee.query.get_or_404(emp_id)

    attendance = Attendance.query.filter_by(
        employee_id=emp_id
    ).order_by(
        Attendance.date.desc()
    ).all()

    return render_template(
        "employee_detail.html",
        emp=emp,
        attendance=attendance
    )


# ================= REPORT =================

@main_routes.route("/report")
def report():

    result = db.session.query(
        Employee.department,
        func.count(Employee.id)
    ).group_by(
        Employee.department
    ).all()

    return render_template(
        "report.html",
        report=result
    )
