#Decision layer (KM-6)
#📄 src/decision/km6_decision_engine.py

from common.models import Decision


class KM6DecisionEngine:
    """
    Implements KM6 Decision Standard v1.0
    """

    def decide(self, validation_results, risk_level: str) -> Decision:
        for result in validation_results:
            if result.status == "FAIL":
                return Decision(
                    outcome="REJECT",
                    justification=result.reason or "Validation failed"
                )

        if risk_level == "high":
            return Decision(
                outcome="ESCALATE",
                justification="High risk requires human approval"
            )

        return Decision(
            outcome="APPROVE",
            justification="All validations passed"
        )
