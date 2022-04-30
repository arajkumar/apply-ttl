import os
from typing import Dict, List, Tuple
from dataclasses import dataclass
# dataclasses cost like tuple, but comes with greater readability.
@dataclass
class File:
    # File basename will be in the following format.
    #  <branch_name>-<build_number>.tar.gz
    path: str
    modified_time: int
    ttl: int = 0

    def branch_name(self) -> str:
        return os.path.basename(self.path).rpartition("-")[0]

    def __lt__(self, other):
        # to create max heap when we do heapify.
        return -self.modified_time < -other.modified_time


