from file import File
from enum import Enum
import random


class ScanResults(Enum):
    BENIGN = "benign"
    MALICIOUS = "malicious"
    UNKNOWN = "unknown"


class Scanner:
    def __init__(self, singleFile: File) -> None:
        self.singleFile = singleFile

    def scan(self) -> ScanResults:
        return random.choice(list(ScanResults))
