from flask import Flask, render_template
from data import get_tickets
from logic import filter_tickets, get_summary_stats
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    tickets = get_tickets()
    flagged_tickets, normal_tickets = filter_tickets(tickets)
    current_time = datetime.now()
    total_open, unassigned, flagged_count = get_summary_stats(tickets)
    return render_template(
        "index.html",
        normal_tickets=normal_tickets,
        flagged_tickets=flagged_tickets,
        last_refreshed=current_time,
        total_open=total_open,
        unassigned=unassigned,
        flagged_count=flagged_count,
    )


if __name__ == "__main__":
    app.run(debug=True)
