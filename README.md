# 🐍 Flask Tutorial: Complete Guide to Building REST APIs

Welcome to the **Flask_Tutorial** repository!  
This project is designed to help beginners learn how to build and test RESTful APIs using Python and Flask.

---

## 📚 Table of Contents

1. [Introduction](#introduction)
2. [Building REST APIs - Part 1 & 2](#building-rest-apis)
3. [Error Handling and Response Codes](#error-handling)
4. [Database Integration with SQLAlchemy](#sqlalchemy-database-setup)
5. [CRUD Operations](#crud-operations)
6. [JWT Authentication](#jwt-authentication)
7. [API Testing using Thunder Client](#api-testing-with-thunder-client)
8. [Installation](#installation)
9. [Running the App](#running-the-app)
10. [License](#license)

---

## 🚀 Introduction

This tutorial walks you through the basics of Flask API development:
- REST API concepts
- Route definitions using Flask
- HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`)
- Response formatting and status codes

---

## 🛠️ Building REST APIs

You will learn to:
- Create basic endpoints using Flask
- Accept data using `request.json`
- Return data using `jsonify()`

---

## ❗ Error Handling

Learn how to:
- Use `try-except` blocks
- Raise custom errors using `abort()`
- Handle and customize `404`, `400`, and `500` responses

---

## 🗃️ SQLAlchemy Database Setup

Covers:
- Connecting Flask to a PostgreSQL database
- Creating tables using SQLAlchemy ORM
- Models, relationships, and migrations

Example URI used:

```bash
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345@localhost:5432/test'
```

## 🔁 CRUD Operations

You’ll implement:

* `POST` → Create a new user
* `GET` → Fetch one or all users
* `PUT/PATCH` → Update user details
* `DELETE` → Remove user or all records

---

## 🔐 JWT Authentication

Learn how to:

* Install and configure `Flask-JWT-Extended`
* Generate access tokens after login
* Protect routes using `@jwt_required()`
* Handle token expiration and refresh tokens

---

## 🧪 API Testing with Thunder Client

Thunder Client is a lightweight REST client for testing APIs directly in VS Code.

### 🔧 Install Thunder Client in VS Code

1. Open **VS Code**
2. Go to the **Extensions** tab (or press `Ctrl+Shift+X`)
3. Search for **Thunder Client**
4. Click **Install**

### 📂 Import Thunder Collection

1. Open **Thunder Client** tab in the VS Code sidebar
2. Click the **"Collections"** tab
3. Click **"Import"**
4. Select the JSON file from this repo (`thunder-collection_Flask tutorial.json`, if included)
5. You can now test all your API endpoints

---

## 🧰 Installation

1. Clone this repo:

```bash
git clone https://github.com/daran6255/Flask_Tutorial.git
cd Flask_Tutorial
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> ⚠️ Make sure PostgreSQL is installed and running locally.

---

## ▶️ Running the App

To start the server:

```bash
python app.py
```

Then access your API at:

```
http://localhost:5000
```

---

## 📄 License

This project is open-source and free to use for educational purposes.

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss your idea.

---

## 🙌 Author

**Dharanidaran A**
[GitHub](https://github.com/daran6255)

---
