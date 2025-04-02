# 📝 To-Do List API with Python & Flask

This project is a clean and minimal **RESTful API** for managing a simple To-Do list, built using **Python**, **Flask**, and **SQLAlchemy**.

🔧 Designed for learning and scalability, this API demonstrates essential CRUD operations — perfect for those beginning backend development or looking to understand how Flask integrates with relational databases.

---

## 🚀 Features

- ✅ Create new tasks
- 🔍 Retrieve all tasks or a specific task by ID
- ♻️ Update task content or completion status
- 🗑 Delete tasks
- 🔒 Modular architecture using Flask Blueprints
- 🧩 SQLAlchemy for ORM and MySQL integration

---

## 🛠 Tech Stack

- **Python 3**
- **Flask**
- **SQLAlchemy**
- **MySQL** (easily adaptable to PostgreSQL or SQLite)
- **REST API best practices**

---

## 📁 Project Structure
```
API-to-do-list-with-python-and-flask/ 
  ├── app.py # Application entry point 
  ├── config/ # Database configuration module 
  │ └── db.py 
  ├── controllers/ # Contains logic for task operations 
  │ └── task_controller.py 
  ├── database/ # Database connection helper 
  │ └── connection.py 
  ├── models/ # SQLAlchemy model(s) 
  │ └── task_model.py 
  ├── routes/ # Flask Blueprints for API routes 
  │ └── task_routes.py 
  └── README.md # Project overview (this file)
```

---

## ▶️ Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/josgard94/API-to-do-list-with-python-and-flask.git

# 2. Navigate to the project directory
cd API-to-do-list-with-python-and-flask

# 3. Create a virtual environment & install dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 4. Set up your MySQL database
# Update config/db.py with your credentials

# 5. Run the app
python app.py
```
---
## 📬 API Endpoints

| Method | Endpoint       | Description              |
|--------|----------------|--------------------------|
| GET    | `/tasks`       | List all tasks           |
| GET    | `/tasks/<id>`  | Retrieve a task by ID    |
| POST   | `/tasks`       | Create a new task        |
| PUT    | `/tasks/<id>`  | Update an existing task  |
| DELETE | `/tasks/<id>`  | Delete a task            |
---
## ⭐ Like it?
Leave a ⭐ if you enjoy it or find it useful!
---
