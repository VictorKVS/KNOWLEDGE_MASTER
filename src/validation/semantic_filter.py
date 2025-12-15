# src/validation/semantic_filter.py

from common.models import ValidationResult


def semantic_validate(content: str) -> ValidationResult:
    if "indefinitely" in content.lower():
        return ValidationResult(status="FAIL", reason="SEMANTIC_CONFLICT")
    return ValidationResult(status="PASS")
