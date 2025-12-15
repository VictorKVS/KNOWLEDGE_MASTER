# src/intake/intake_handler.py

from common.models import KnowledgeItem
from common.errors import IntakeError


class IntakeHandler:
    """
    Implements Knowledge Intake Standard v1.0
    """

    def accept(self, item: KnowledgeItem) -> KnowledgeItem:
        if not item.metadata.get("source_id"):
            raise IntakeError("Missing source attribution")

        # Candidate knowledge only
        return item
