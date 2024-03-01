import datetime
from dataclasses import dataclass


@dataclass
class Content:
    title: str
    content: str
    author: str
    created_time: datetime