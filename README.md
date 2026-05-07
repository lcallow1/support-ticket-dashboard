# Ticket Dashboard

A simple Flask-based dashboard that flags unassigned support tickets that have been waiting longer than a set threshold (default 30 minutes) and present tickets that are in an updated state (customer waiting).

## Features

- Highlights unassigned tickets that have been waiting too long
- Highlights tickets in an update state which means the customer has replied
- Displays time waiting per ticket in a readable format with color codes
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
4. Install dependencies
5. Run the app:
   `python app.py`
6. Open `http://127.0.0.1:5000` in your browser

## Project Structure

- `app.py` — Flask app and routing
- `data.py` — ticket data source (HaloPSA API)
- `logic.py` — filtering and time calculation logic
- `templates/index.html` — main dashboard template
- `static/` — CSS and images
