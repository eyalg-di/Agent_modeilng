from enum import Enum
import random
from file import File


def getRemediationType(singleFile: File):
    return random.choice(list(RemediationType))


def remediate(singleFile: File):
    if getRemediationType(singleFile) is RemediationType.DELETE:
        _delete(singleFile)
    else:
        _quarantine(singleFile)


def _quarantine(singleFile: File):
    singleFile.quarantine()


def _delete(singleFile: File):
    singleFile.delete()


class RemediationType(Enum):
    DELETE = "delete"
    QUARANTINE = "quarantine"
