A simple Todo application built with Django for managing daily tasks.

Other language documantion : [Persian](https://github.com/iamcloner/django-todo/blob/main/README-FA.md)

## 📌 Features
 - Create, edit, and delete tasks
 - Categorize tasks into different sections
 - Unit tests to ensure proper functionality
 - Simple and user-friendly interface

## ⚙️ Requirements
To run this project, you need:
Python 3.8 or higher
Django 3.2 or higher
SQLite database (default)

## 🚀 Setup Instructions
Clone the repository:
```bash
git clone https://github.com/iamcloner/django-todo.git
cd django-todo
```

Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Apply database migrations:
```bash
python manage.py migrate
```

Create a superuser account:
```bash
python manage.py createsuperuser
```

Run the development server:
```bash
python manage.py runserver
```

Now you can access the app at `http://127.0.0.1:8000`

## 🛠️ Usage

To access the admin panel, go to `http://127.0.0.1:8000/admin`
 and log in with your superuser account.

In the admin panel, you can create new tasks, categorize them, edit them, or delete them.

## 🤝 Contributing

We welcome contributions! To contribute:

 - Fork the repository
 - Create a new branch for your feature or fix
 - Commit your changes
 - Open a Pull Request and describe your changes

## 📄 License

This project is licensed under the MIT License.
