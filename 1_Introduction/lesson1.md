# Flask Notes

## What is Flask?

**Flask** is a tool made with **Python** that helps you create **websites and web apps**.

- It is a **small and simple** tool (called a micro-framework).
- You can **add only what you need**, like a database or login system.
- Built on two important parts:
  - **Werkzeug**: Helps connect your app to the internet.
  - **Jinja2**: Helps create HTML pages using templates.

> In short, Flask helps you build websites using Python with less code and more control.

----

## Why Should You Use Flask?

- **Very simple**: Easy to learn and use.
- **Add only what you need**: You are in control of the features.
- **Great for beginners**: Perfect for learning how web apps work.
- **Good for APIs**: Easy to make apps that talk to other apps (like mobile or other websites).

----

## Summary

| Feature       | Flask (Simple Meaning)                          |
|---------------|-------------------------------------------------|
| What is it?   | A tool to build websites using Python.          |
| Why use it?   | Easy to use, flexible, and great for beginners. |
| Good for?     | Small to medium projects and web APIs.          |


----

## Flask vs Django (Quick Overview)

| Feature           | Flask                          | Django                         |
|------------------|---------------------------------|--------------------------------|
| Type             | Micro-framework                 | Full-stack framework           |
| Flexibility      | High – you choose components    | Low – built-in components      |
| Learning Curve   | Easier for beginners            | Steeper learning curve         |
| Admin Panel      | Not included by default         | Comes with a powerful admin UI |
| Use Case         | Small to medium apps, APIs      | Large applications, enterprise |

---

## Installing Flask and Setting Up Environment

	### Step 1: Create a virtual environment
	python -m venv venv

	### Step 2: Activate the environment
	venv\Scripts\activate

	### Step 3: Install Flask
	pip install Flask

	### Step 4: Check if Flask is installed
	flask --version

----

## Creating Your First Flask App (Hello World)
1. create file name as app.py in your project folder
2. paste the below code in the app.py file
3. run the app.py by 
	python app.py

----

## simple project structure for flask
my_flask_app/
│
├── app.py                # Main application file (entry point)
├── templates/            # HTML templates folder (for rendering pages)
│   └── index.html        # A sample HTML file
├── static/               # Static files like CSS, JS, and images
│   └── style.css         # A sample CSS file
├── venv/                 # Virtual environment (auto-created)
└── requirements.txt      # List of project dependencies
----