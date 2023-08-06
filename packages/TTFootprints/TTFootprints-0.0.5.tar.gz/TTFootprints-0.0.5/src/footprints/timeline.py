from typing import List
from footprints import ticket
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Event():
    agent: str
    timestamp: datetime
    ticket_number: int

Timeline = List[Event]

def print_event(event: Event):
    print("{0}, {1}, {2}".format(event.ticket_number, event.agent, event.timestamp))

def make_timeline(tickets: List[ticket.Ticket]) -> Timeline:

    events = []

    for tick in tickets:
        for upd in ticket.make_updates(tick.data["Description"]):
            events.append(Event(upd.author, upd.timestamp, tick.data["Ticket Number"]))

    return sorted(events, key=lambda t: t.timestamp)

