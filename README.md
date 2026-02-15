# 🚀 HRMS – Human Resource Management System (Flask)

A modern, scalable, and production-ready **HRMS (Human Resource Management System)** built using **Flask, SQLAlchemy, and REST APIs**.

This project simulates a real-world HR platform for managing employees, attendance, and departmental reports with both **Web UI and API support**.

---

## 📌 Key Highlights

✅ Clean Architecture (App Factory Pattern)  
✅ RESTful API Design  
✅ Professional Dashboard UI  
✅ ORM-based Database Management  
✅ Attendance Automation  
✅ Department Analytics  
✅ Scalable & Maintainable Codebase  
✅ Industry-Standard Practices  

---

## ✨ Features

### 👨‍💼 Employee Management
- Add new employees
- View employee list
- View detailed employee profiles
- Email uniqueness validation

### ⏰ Attendance Management
- Check-In / Check-Out system
- Daily attendance tracking
- Individual attendance history
- API-based attendance marking

### 📊 Reports & Analytics
- Department-wise employee count
- Visual dashboard overview
- Real-time statistics

### 🌐 REST APIs
- Employee creation
- Attendance management
- Health monitoring
- JSON-based data exchange

### 🎨 User Interface
- Modern glassmorphism design
- Responsive layout
- Flash notifications
- User-friendly navigation

---

## 📁 Project Structure
```
hrms_project/
│
├── app/
│ ├── init.py # App Factory & DB Initialization
│ ├── models.py # Database Models
│ ├── routes.py # Frontend Routes
│ ├── api.py # REST API Endpoints
│ └── config.py # Configuration
│
├── templates/ # HTML Templates
│ ├── base.html
│ ├── home.html
│ ├── employees.html
│ ├── attendance.html
│ ├── employee_detail.html
│ └── report.html
│
├── static/ # Static Assets
│ ├── css/style.css
│ └── js/main.js
│
├── app.py # Development Runner
├── run.py # Production Runner
├── requirements.txt # Dependencies
└── README.md # Documentation
```

---

## ⚙️ Tech Stack

| Layer        | Technology |
|--------------|------------|
| Backend      | Flask (Python) |
| ORM          | SQLAlchemy |
| Migration    | Flask-Migrate |
| Database     | SQLite / PostgreSQL |
| API Testing  | Thunder Client / Postman |
| Frontend     | HTML, CSS, JS |
| Architecture | App Factory Pattern |

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone <repository-url>
cd hrms_project
```
### 2️⃣ Create Virtual Environment
```
python -m venv venv
```
* Activate:
Windows
```
venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
---
## Database Setup
Run the following commands:
```
flask db init
flask db migrate
flask db upgrade
```
This will create all required tables.

## ▶️ Run the Application
#### Development Mode
```
python app.py
```
#### Production Mode
```
python run.py
```


#### Server will start at:
```
http://127.0.0.1:5000
```
---
## 🌐 Web Application Routes
| Route           | Description         |
| --------------- | ------------------- |
| /               | Dashboard           |
| /employees      | Employee Management |
| /attendance     | Attendance System   |
| /employees/<id> | Employee Details    |
| /report         | Department Report   |

---
## 🔗 REST API Endpoints
* Health Check
```
GET /api/health
```
* Create Employee
```
POST /api/employees

Body (JSON):

{
  "name": "John Doe",
  "email": "john@gmail.com",
  "designation": "Developer",
  "department": "IT",
  "address": "Bangalore"
}
```
* Mark Attendance
```
POST /api/attendance
{
  "employee_id": 1,
  "in_time": "09:30",
  "out_time": "18:00"
}

```
* Get Attendance
```
GET /api/attendance/<employee_id>

```
---
## API Testing

#### You can test APIs using:
* Thunder Client (VS Code)
* Postman
* curl

##### Example:
* curl http://127.0.0.1:5000/api/health

---
### Documentation
* ✔ All models and routes are documented using docstrings 
* ✔ Clean naming conventions
* ✔ PEP-8 compliant code
* ✔ Modular architecture
---
### Production Readiness
###### This system supports:

* API-first development
* Mobile/Web integration
* Role expansion
* Analytics extension
* Cloud deployment
* Ready for scaling
---
### Future Enhancements
* Admin Role Management
* Authentication & Authorization
* AI Attendance Analytics
* Payroll System
* Performance Tracking
* Cloud Deployment
* Microservices Support

---
## 👨‍💻 Developer
### Rohit Kumar Rai
* Backend Developer | Python | Flask | APIs
