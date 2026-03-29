# Day 11 - Django Web Framework

## Assignment

Build a **Django web application** that accepts user input through a form, runs a prediction, and displays the result — using the **Titanic survival prediction** as the use case.

### Project Structure

```
Day 11 - Django Web Framework/
├── manage.py                  ← Django management entry point
├── db.sqlite3                 ← SQLite database
├── titanic_project/           ← Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── predictor/                 ← Django app
    ├── views.py               ← handles form input & prediction logic
    ├── models.py              ← data models
    ├── fake_model.py          ← mock ML model for prediction
    ├── admin.py
    ├── apps.py
    ├── migrations/
    └── templates/
        ├── index.html         ← input form
        └── result.html        ← prediction result page
```

### Tasks

1. Set up a Django project (`titanic_project`) with a single app (`predictor`).
2. Create a form (`index.html`) that accepts passenger features:
   - Passenger class (1st, 2nd, 3rd)
   - Sex (Male / Female)
   - Age
   - Number of siblings/spouses aboard (SibSp)
   - Fare
3. In `views.py`, receive the form data and pass it to a prediction function.
4. Display the prediction result (Survived / Did Not Survive) on `result.html`.
5. Configure `urls.py` to route `/` to the input form and `/predict` to the result.

### Running the Project

```bash
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.
