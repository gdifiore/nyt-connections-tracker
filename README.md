# NYT Connections Tracker

Track your NYT Connections results. Paste your results to see which categories you get right most often.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python app.py
```

## Tests

```bash
pytest tests/ -v
```

## Deploy

Uses Heroku. Set `FLASK_SESSION_SECRET` in config vars.

<img src="docs/Screenshot 2024-12-26 154015.png" width="45%"> <img src="docs/Screenshot 2024-12-26 154036.png" width="45%">