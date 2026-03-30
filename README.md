# SkillSakhi - Demographic-Aware Career and Skill Recommendation Platform

SkillSakhi is a production-oriented full-stack web application that helps women start/restart careers through personalized career recommendations, skill-gap insights, course suggestions, and job opportunities.

## Tech Stack
- **Frontend:** React, Axios, Recharts, CSS
- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL (SQLite fallback for local quick start)
- **ML:** Pandas, NumPy, Scikit-learn (KNN classifier)

## Project Structure

```text
skillsakhi_backend/
  manage.py
  skillsakhi/
  users/
  recommendations/
  ml_model/
  data/
skillsakhi_frontend/
  public/
  src/
    components/
    pages/
    services/
    charts/
```

## Backend Features
- Registration/login using token auth
- Profile capture (age, education, location, interests, skills, work preference)
- Hybrid recommendation engine:
  - Rule-based suggestions
  - ML prediction using KNN model
- Skill-gap analysis with skill-match percentage
- Career-linked courses and jobs

## API Endpoints
- `POST /api/register`
- `POST /api/login`
- `POST /api/profile`
- `GET /api/profile/me`
- `GET /api/career-recommendation`
- `GET /api/skill-gap`
- `GET /api/courses`
- `GET /api/jobs`

## Dataset
Sample dataset for training ML model: `skillsakhi_backend/data/career_dataset.csv`

Columns:
- `age`
- `education`
- `interests`
- `work_preference`
- `career`
- `required_skills`
- `demand_level`

## Local Setup

### 1) Clone and install backend dependencies
```bash
cd skillsakhi_backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2) Configure environment
```bash
export POSTGRES_DB=skillsakhi_db
export POSTGRES_USER=skillsakhi_user
export POSTGRES_PASSWORD=skillsakhi_password
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
# Optional quick local fallback:
# export USE_SQLITE=1
```

### 3) Run migrations and seed data
```bash
python manage.py makemigrations
python manage.py migrate
python ml_model/train_model.py
python manage.py seed_data
python manage.py runserver
```

### 4) Run frontend
```bash
cd ../skillsakhi_frontend
npm install
npm start
```

Frontend runs on `http://localhost:3000` and backend on `http://localhost:8000`.

## Deployment Instructions

### Backend deployment (example: Render, Railway, EC2)
1. Provision PostgreSQL database.
2. Set env vars (`DJANGO_SECRET_KEY`, DB credentials, `DJANGO_DEBUG=0`, `DJANGO_ALLOWED_HOSTS`).
3. Install dependencies and run:
   - `python manage.py migrate`
   - `python ml_model/train_model.py`
   - `python manage.py seed_data`
4. Run with gunicorn:
   - `gunicorn skillsakhi.wsgi:application --bind 0.0.0.0:8000`

### Frontend deployment (example: Vercel/Netlify)
1. Set `REACT_APP_API_URL=https://<backend-domain>/api`
2. Build and deploy:
   - `npm install`
   - `npm run build`

## Notes for Production Hardening
- Add robust validation and structured logging.
- Add JWT refresh flow if needed.
- Add Redis caching for recommendations.
- Integrate real course/job provider APIs.
- Add role-based admin UI for data curation.
