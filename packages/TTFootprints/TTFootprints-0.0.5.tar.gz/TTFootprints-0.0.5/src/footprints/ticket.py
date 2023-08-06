from dataclasses import dataclass
from typing import Dict, List
from datetime import datetime, timedelta
import csv

from footprints import util

@dataclass
class Ticket():
    data: Dict

@dataclass
class Update():
    body: str
    author: str
    timestamp: datetime

def keys(ticket: Ticket) -> List[str]:
    return ticket.data.keys()

def has_key(ticket: Ticket, key: str) -> bool:
    return key in keys(ticket)

def make_update(description: str) -> Update:
    timestamp_str   = util.extract_between(description, None, "EDT", right_adjust=-1)
    timestamp       = datetime.strptime(timestamp_str, "%m/%d/%Y at %H:%M:%S")
    body            = util.extract_between(description, "\n", None)
    author          = util.extract_between(description, " by ", "\n", left_adjust=4, right_adjust=-1)
    return Update(body, author, timestamp)

def make_updates(full_description: str) -> List[Update]:
    updates = full_description.split("Entered on ")[1:]
    return [make_update(update) for update in updates]

def ticket_duration(ticket: Ticket) -> timedelta:
    updates = make_updates(ticket.data["Description"])
    return updates[0].timestamp - updates[len(updates)-1].timestamp

def read_csv(file_location: str) -> List[Ticket]:
    with open(file_location, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        return [Ticket(row) for row in reader]