# Cyber-Crime-Reporting-and-Awareness-Portfolio
# 🛡️ Cyber Crime Reporting & Awareness Portal (CCR)

A web-based Cyber Crime Reporting and Awareness Portal developed using **Django (Python)**.  
This system allows users to report cyber crimes, track complaint status, and view cyber awareness posts.  
An Admin Panel is provided to manage complaints and publish awareness content.

---

## 📌 Project Objective

The objective of this project is to:

- Provide an online platform for reporting cyber crimes
- Allow users to track complaint status
- Enable administrators to manage complaints
- Spread cyber awareness through informative posts
- Promote safe digital practices

---

## 🚀 Features

### 👤 User Module
- User Registration
- User Login & Logout
- Report Cyber Crime
- View Complaint Status
- Access Cyber Awareness Posts

### 🛠️ Admin Module (Custom Admin Panel)
- Admin Login
- Dashboard Overview
- View All Complaints
- Update Complaint Status (Pending / Resolved)
- Add & Manage Awareness Posts

---

## 🧰 Technology Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS (Custom Styled Templates)
- **Database:** SQLite3
- **Authentication:** Django Authentication System

---

## 📂 Project Structure
CCR/
│
├── CCR/ # Main Project Folder
│
├── users/ # User Module
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│
├── adminpanel/ # Custom Admin Module
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│
├── crimereporting/ # Complaint & Awareness Models
│ ├── models.py
│
├── templates/
│
└── manage.py

