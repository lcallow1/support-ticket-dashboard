from datetime import datetime


def filter_tickets(tickets):
    flagged_tickets = []
    normal_tickets = []
    for ticket in tickets:
        agent_id = ticket["agent_id"]
        converted_time = datetime.strptime(ticket["created_at"], "%Y-%m-%d %H:%M")
        seconds = (datetime.now() - converted_time).total_seconds()
        hours = (seconds % 86400) // 3600
        minutes = (seconds % 3600) // 60
        days = seconds // 86400
        if days > 0:
            ticket["time_waiting"] = f"{days:.0f}d:{hours:02.0f}:{minutes:02.0f}"
        else:
            ticket["time_waiting"] = f"{hours:02.0f}:{minutes:02.0f}"
        if (
            agent_id is None
            and (datetime.now() - converted_time).total_seconds() > 1800
        ):
            flagged_tickets.append(ticket)
        else:
            normal_tickets.append(ticket)
    return flagged_tickets, normal_tickets
