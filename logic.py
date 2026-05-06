from datetime import datetime, timezone


def filter_tickets(tickets):
    flagged_tickets = []
    normal_tickets = []
    for ticket in tickets:
        agent_id = ticket["agent_id"]
        converted_time = datetime.fromisoformat(ticket["created_at"]).replace(
            tzinfo=timezone.utc
        )
        seconds = (datetime.now(timezone.utc) - converted_time).total_seconds()
        hours = (seconds % 86400) // 3600
        minutes = (seconds % 3600) // 60
        days = seconds // 86400
        if days > 0:
            ticket["time_waiting"] = f"{days:.0f}d:{hours:02.0f}:{minutes:02.0f}"
        else:
            ticket["time_waiting"] = f"{hours:02.0f}:{minutes:02.0f}"
        if agent_id is None and seconds > 1800:
            flagged_tickets.append(ticket)
        else:
            normal_tickets.append(ticket)
    return flagged_tickets, normal_tickets


def get_summary_stats(tickets):
    total_open = len(tickets)
    unassigned_tickets = 0
    for t in tickets:
        if t["agent_id"] == None:
            unassigned_tickets += 1
    flagged, _ = filter_tickets(tickets)
    flagged_count = len(flagged)
    return total_open, unassigned_tickets, flagged_count
