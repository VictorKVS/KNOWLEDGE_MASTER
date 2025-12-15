#src/common/errors.py

class KnowledgeError(Exception):
    pass


class IntakeError(KnowledgeError):
    pass


class ValidationError(KnowledgeError):
    pass


class DecisionError(KnowledgeError):
    pass
