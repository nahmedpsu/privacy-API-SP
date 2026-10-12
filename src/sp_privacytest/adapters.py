"""Future operator-approved adapter boundary; deliberately non-operational."""

from typing import Protocol


class MISAdapter(Protocol):
    """Interface only; implementations must enforce a separate approved safety policy."""

    def execute(self, contract: dict) -> dict:
        """Execute only within explicit owner-approved scope and retain raw data locally."""
        ...


class UnavailableAdapter:
    def execute(self, contract: dict) -> dict:
        raise NotImplementedError(
            "No live adapter is provided. Owner authorization and implementation are required."
        )
