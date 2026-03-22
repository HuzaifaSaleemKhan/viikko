# Viikkonumero 🇫🇮

Finnish week number web app built with Streamlit.
Supports Finnish, Swedish, and English.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Cloud (free)

1. Push this folder to a GitHub repository
2. Go to https://share.streamlit.io
3. Connect your GitHub repo and select `app.py`
4. Click Deploy — your app gets a public URL instantly

## Deploy to other platforms

**Heroku / Railway / Render:**
Add a `Procfile`:
```
web: streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

## Features
- Current ISO 8601 week number
- Week date range (Monday – Sunday)
- Day of year & days remaining
- All Finnish public holidays 2026 with week numbers
- Language switcher: Finnish / Swedish / English
