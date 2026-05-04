# DentAssure — UK Dental Indemnity Risk Assessment System (Django)

**Author:** Alfred Divine  
**Stack:** Python · Django · SQLite · Groq API  
**Task:** AIA Candidate Practical Test — UK Dental Indemnity Build

---

## Flow

```
User fills form → JS calls Groq API → AI returns JSON risk result
→ Django POST /api/leads saves to SQLite → Result displayed → Table refreshes
```

--- 

## Setup & Run

### 1. Install dependencies
```bash
pip install django
```

### 2. Set your Groq API key
```bash
# Mac/Linux
export GROQ_API_KEY="gsk-your-key-here"

# Windows
set GROQ_API_KEY=gsk-your-key-here
```

### 3. Apply migrations
```bash
python manage.py migrate
```

### 4. Run the server
```bash
python manage.py runserver
```

### 5. Open in browser
```
http://localhost:8000
```

---

## Project Structure

```
dentassure/
├── manage.py
├── requirements.txt
├── leads.db                  ← auto-created on first run
├── dentassure/
│   ├── settings.py
│   ├── urls.py
│   └── gateway.py
└── leads/
    ├── models.py             ← Lead model
    ├── views.py              ← index + REST API views
    ├── urls.py               ← URL routing
    ├── apps.py
    ├── migrations/
    │   └── 0001_initial.py
    └── templates/leads/
        └── index.html        ← Full frontend UI
```

---

## API Endpoints

| Method | URL          | Description            |
|--------|-------------|------------------------|
| GET    | `/`          | Web interface          |
| POST   | `/api/leads` | Save classified lead   |
| GET    | `/api/leads/`| Return all leads JSON  |

---

## Django Admin

Create a superuser to browse leads in the Django admin:
```bash
python manage.py createsuperuser
# Visit: http://localhost:8000/admin
```

---

## Design Decisions

- **Django ORM** — Lead model with proper field types and choices; JSONField for risk_factors
- **Environment variables** — Groq API key stored in `.env` file via `django-environ`, injected into the template via Django context (`{{ api_key }}`). Never hardcoded or committed to version control.
- **CSRF** — Django CSRF token read from cookie and sent with POST via `X-CSRFToken` header
- **SQLite** — zero-config for POC; swap to PostgreSQL in production via `settings.py`
- **Single app architecture** — clean `leads` app handles models, views, URLs, and templates

---

## Time Taken
~3 hours (design + build + test)
