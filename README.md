# Loan Eligibility Checker

A simple Django web application that allows users to apply for loans and get an eligibility result based on their financial details. 
The form is styled using Bootstrap for a clean and responsive user interface.

---

## Features

- Submit loan applications through a web form
- Automatically evaluate eligibility based on income, debt, credit score, and loan amount
- View the eligibility result after submission
- Styled with Bootstrap 4

---

## Technologies Used

- Python 3.x
- Django 3.x or 4.x
- Bootstrap 4
- MySQL 

---

## Setup Instructions

### 1. Clone the repository

bash
git clone https://github.com/your-username/loan-eligibility-checker.git
cd loan-eligibility-checker

### 2. Create a virtual environment and activate it

python -m venv env
# On Windows
env\Scripts\activate
# On macOS/Linux
source env/bin/activate

### 3. Install dependencies
pip install django

### 4. Install a database server 
Create an empty database and with a database server like MySQL
and use your credentials to connect in the /loanpredictor/loanpredictor/settings.py file 
in the DATABASE SECTION looking something like this

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',    # Tell Django to use MySQL
        'NAME': 'loan_eligibility',               # Your database name
        'USER': 'root',                           # Your MySQL username (usually 'root')
        'PASSWORD': '',                           # Your MySQL password 
        'HOST': '127.0.0.1',                      # Localhost
        'PORT': '3306',                           # Default MySQL port
    }
}

### 5. Apply Migrations
python manage.py migrate

### 6. Run the development server
python manage.py runserver

Then open your browser and go to http://127.0.0.1:8000/ 




