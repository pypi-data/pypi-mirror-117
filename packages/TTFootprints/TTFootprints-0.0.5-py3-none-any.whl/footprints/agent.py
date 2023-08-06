from dataclasses import dataclass
from typing import List

from footprints import ticket

Agent = str

@dataclass
class AgentStats():
    agent: Agent
    updates: List[ticket.Update]
