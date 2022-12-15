from dataclasses import dataclass


@dataclass
class Register:
    id: str
    name: str
    last_name: str
    document: str
    date: str
    result: str
