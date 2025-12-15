#5️⃣ Test Executor (core)
#📄 src/tests_runner/executor.py

from common.models import KnowledgeItem
from adapters.ai_adapter import AIAdapter
from tests_runner.assertions import assert_equals


class TestExecutor:
    """
    Executes tests-as-law against code skeleton
    """

    def run_contract_test(self, test: dict):
        adapter = AIAdapter()

        given = test["given"]
        when = test["when"]
        then = test["then"]

        item = KnowledgeItem(
            content="test",
            metadata={
                "source_id": given.get("source_type"),
                "trust_level": given.get("trust_level"),
            }
        )

        decision = adapter.handle_request(
            knowledge_item=item,
            risk_level=given.get("trust_level", "low")
        )

        assert_equals(
            decision.outcome,
            then["decision"],
            "Decision outcome mismatch"
        )

    def run(self, test: dict):
        test_id = test.get("test_id", "UNKNOWN")

        if test_id.startswith("CT-"):
            self.run_contract_test(test)
        else:
            raise NotImplementedError(f"Test type not supported: {test_id}")