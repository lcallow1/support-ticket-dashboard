# Ticket Dashboard

A simple Flask-based dashboard that flags unassigned support tickets that have been waiting longer than a set threshold (default 30 minutes).

## Features

- Highlights unassigned tickets that have been waiting too long
- Displays time waiting per ticket in a readable format
- Auto-refreshes every 60 seconds
- Last refreshed timestamp
- Scrollable tables with sticky headers
- Empty state when no tickets are flagged

## Tech Stack

- Python
- Flask
- Jinja2 templates
- HTML/CSS

## Getting Started

1. Clone the repo
2. Create a virtual environment:
   `python -m venv venv`
3. Activate it (Windows):
   `venv\Scripts\activate`
4. Install dependencies:
   `pip install flask`
5. Run the app:
   `python app.py`
6. Open `http://127.0.0.1:5000` in your browser

## Project Structure

- `app.py` — Flask app and routing
- `data.py` — ticket data source (currently mock data, will be swapped for HaloPSA API)
- `logic.py` — filtering and time calculation logic
- `templates/index.html` — main dashboard template
- `static/` — CSS and images

## Roadmap

- Connect to HaloPSA API for live ticket data
- Detect tickets where customer is waiting for a reply
- Configurable alert threshold
- Sort by time waiting
