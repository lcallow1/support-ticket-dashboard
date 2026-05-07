from flask import Flask, render_template
from data import get_tickets, get_agents
from logic import get_flagged_tickets, get_summary_stats, get_updated_tickets
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    agents = get_agents()
    tickets = get_tickets(agents)
    flagged_tickets = get_flagged_tickets(tickets)
    current_time = datetime.now()
    updated_tickets = get_updated_tickets(tickets)
    total_open, flagged_count = get_summary_stats(tickets, flagged_tickets)
    updated_count = len(updated_tickets)
    return render_template(
        "index.html",
        flagged_tickets=flagged_tickets,
        last_refreshed=current_time,
        total_open=total_open,
        flagged_count=flagged_count,
        updated_tickets=updated_tickets,
        updated_count=updated_count,
    )


if __name__ == "__main__":
    app.run(debug=True)
