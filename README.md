## Engineering Evaluation API

The Engineering Evaluation API is a backend system developed as part of the ALX Backend Engineering Capstone Project. The API provides a way to manage company engineering projects, student submissions, and project evaluations.

The system allows companies to create engineering projects, students to submit their work, and companies to review and score those submissions.

### Features

User registration and authentication

Role-based access control (students and companies)

Creating and managing engineering projects

Submission of project solutions

Evaluation of student submissions

### Technologies Used

Python

Django

Django REST Framework

SQLite database

### API Endpoints
#### Authentication
POST /api/register/
POST /api/login/

#### Projects
GET  /api/projects/
POST /api/projects/
PUT  /api/projects/{id}/
DELETE /api/projects/{id}/

#### Submissions
GET  /api/submissions/
POST /api/submissions/

#### Evaluations
GET  /api/evaluations/
POST /api/evaluations/

### Installation

git clone https://github.com/yourusername/engineering-evaluation_api-capstone-project.git
cd engineering-evaluation_api-capstone-project
python -m venv venv
source venv/bin/activate

### Install dependencies:

pip install -r requirements.txt

### Apply migrations:

python manage.py migrate


### Run the development server:

python manage.py runserver

### Deployment

The project is deployed using:

PythonAnywhere

## Author

Believe Mukomberanwa

ALX Backend Engineering Student
