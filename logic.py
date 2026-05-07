from datetime import datetime, timezone


def get_time_waiting(ticket):
    converted_time = datetime.fromisoformat(ticket["created_at"]).replace(
            tzinfo=timezone.utc)
    seconds = (datetime.now(timezone.utc) - converted_time).total_seconds()
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    days = seconds // 86400
    if days > 0:
        ticket["time_waiting"] = f"{days:.0f}d:{hours:02.0f}:{minutes:02.0f}"
    else:
        ticket["time_waiting"] = f"{hours:02.0f}:{minutes:02.0f}"
    return ticket, seconds

def get_flagged_tickets(tickets):
    flagged_tickets = []
    for ticket in tickets:
        _, seconds = get_time_waiting(ticket)
        agent_id = ticket["agent_id"]
        if agent_id is None and seconds > 1800:
            flagged_tickets.append(ticket)
    return flagged_tickets


def get_updated_tickets(tickets):
    updated_tickets = []
    for ticket in tickets:
        get_time_waiting(ticket)
        agent_id = ticket["agent_id"]
        status_id = ticket["status_id"]
        if agent_id is not None and status_id == 22:
            updated_tickets.append(ticket)
    return updated_tickets


def get_summary_stats(tickets, flagged_tickets):
    total_open = len(tickets)
    flagged_count = len(flagged_tickets)
    return total_open, flagged_count


