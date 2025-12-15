# src/validation/security_filter.py

from common.models import ValidationResult


def security_validate(content: str) -> ValidationResult:
    if "IGNORE ALL PREVIOUS" in content.upper():
        return ValidationResult(status="FAIL", reason="PROMPT_INJECTION")
    return ValidationResult(status="PASS")
