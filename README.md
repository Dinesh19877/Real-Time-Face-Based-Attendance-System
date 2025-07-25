

# 🎯 Real-Time Face-Based Attendance System using Django

This innovative **Real-Time Face-Based Attendance System** utilizes Django’s robust backend capabilities integrated with cutting-edge facial recognition to automate and streamline the attendance process. By leveraging machine learning, OpenCV, and face recognition libraries, the system ensures high accuracy and efficiency in tracking and verifying student presence — ideal for modern classrooms and institutional settings.

---

## 🚀 Features

* 🔍 Real-time face detection & recognition
* ✅ Automatic attendance marking
* 🤖 Machine learning-powered facial verification
* 🌐 Django-based web application
* 🔐 Secure admin login & access control
* 🗃️ Attendance records stored in SQLite/MySQL
* 🔄 Scalable and modular codebase
* 📷 Live camera/webcam integration
* 📊 Attendance logs with reporting
* 🖥️ Cross-platform & browser compatible

---

## 🛠️ Prerequisites

### 📌 Technical Requirements

* Python 3.6+
* Basic knowledge of Python, Django, HTML/CSS
* A functional webcam (internal or external)

### 📌 Libraries to Install

```bash
pip install django
pip install opencv-python
pip install dlib
pip install face_recognition
pip install numpy
```

### 📌 Tools & Environment

* IDE: VS Code / PyCharm
* Database: SQLite (default with Django)
* Web browser for interface access
* Git (for version control)

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Dinesh19877/Real-Time-Face-Based-Attendance-System.git
cd Real-Time-Face-Based-Attendance-System
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate the Virtual Environment

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```

* **Linux/Mac:**

  ```bash
  source venv/bin/activate
  ```

### 4️⃣ Install Dependencies

```bash
pip install django opencv-python dlib face_recognition numpy
```

### 5️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to set your admin credentials.

### 7️⃣ Run the Server

```bash
python manage.py runserver
```

### 🔗 Access the Web App

* **Admin Panel:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **User Login Panel:** [http://127.0.0.1:8000/User\_login/](http://127.0.0.1:8000/User_login/)

---

## 📁 Project Structure

```
├── app1/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── media/  ← for storing face images
├── static/ ← CSS/JS files
├── db.sqlite3
├── manage.py

```


