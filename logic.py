from datetime import datetime, timezone

#Takes a ticket, figures out how long it's been open, and adds a human-readable time_waiting string to it
def get_time_waiting(ticket):
    #Convert Halo string into Python datetime object and make it utc
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
    if seconds < 3600:
        ticket["time_tier"] = "fresh"
    elif seconds < 14400:
        ticket["time_tier"] = "warning"
    else:
        ticket["time_tier"] = "critical"
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


