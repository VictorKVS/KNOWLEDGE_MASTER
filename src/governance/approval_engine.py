#src/governance/approval_engine.py

def requires_human_approval(risk_level: str) -> bool:
    return risk_level.lower() == "high"