**1) Student Management API:**

A RESTful Student Management API built with Python and FastAPI.
This project provides APIs for managing student records through a simple and structured backend application.

**2) Features:**

Create a new student

Retrieve all students

Retrieve a student by ID

Update student information

Delete a student

Data validation using Pydantic

RESTful API endpoints

Interactive API documentation with Swagger UI

**3) Technologies Used:**

Python

FastAPI

Pydantic

SQLAlchemy

MySQL

PyMySQL

Uvicorn

**4) Installation:-**

**Clone the repository:**
git clone https://github.com/ih8asham/student-management-api.git

**Go to the project directory:**
cd student-management-api

**Create a virtual environment:**
python -m venv venv

**Activate the virtual environment on Windows:**
venv\Scripts\activate

**Install the required packages:**
pip install -r requirements.txt

**5) Database Configuration:-**

Configure your MySQL database credentials in the project's database configuration.

**Example:**
DB_USER = "root"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "student_db"
Do not upload real passwords or sensitive credentials to GitHub.

**6) Run the API:-**

**Start the FastAPI server:**
uvicorn main:app --reload

**The API will run at:**
http://127.0.0.1:8000

**7) API Documentation:-**

**After starting the server, open:**
http://127.0.0.1:8000/docs
Swagger UI allows you to view and test the available API endpoints.

**Alternative documentation:**
http://127.0.0.1:8000/redoc


**Author:**

Muhammad Ihtasham

**GitHub:** https://github.com/ih8asham
