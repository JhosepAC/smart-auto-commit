from enum import Enum


class ApplicationStatus(Enum):
    """
    Application lifecycle states.
    """

    CREATED = "created"
    INITIALIZING = "initializing"
    RUNNING = "running"
    FAILED = "failed"
    STOPPED = "stopped"
