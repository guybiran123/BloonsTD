from dataclasses import dataclass


@dataclass
class Direction:
    """
    A data class that represents the direction we draw an object.
    """
    does_matter: bool
    value: float
