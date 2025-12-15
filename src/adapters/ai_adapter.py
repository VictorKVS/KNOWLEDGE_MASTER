#7️⃣ Adapter layer (AI / UAG)
# 📄 src/adapters/ai_adapter.py

from intake.intake_handler import IntakeHandler
from decision.km6_decision_engine import KM6DecisionEngine


class AIAdapter:
    """
    Adapter between AI / UAG and Knowledge Master
    """

    def handle_request(self, knowledge_item, risk_level):
        intake = IntakeHandler()
        candidate = intake.accept(knowledge_item)

        decision_engine = KM6DecisionEngine()
        return decision_engine.decide([], risk_level)