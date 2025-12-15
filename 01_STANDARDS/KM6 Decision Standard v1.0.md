#KNOWLEDGE_MASTER/01_STANDARDS/KM6_Decision_Standard_v1.0.md


📘 KM6 Decision Standard v1.0
KNOWLEDGE_MASTER / MindForge

Статус: Mandatory
Версия: 1.0
Уровень: Enterprise / Decision Governance
Область: Knowledge-Based Decision Making
Роль: KM-6 (Knowledge Master)

1. Назначение стандарта
Данный стандарт определяет обязательный процесс принятия решений в системе KNOWLEDGE_MASTER на основе:

Knowledge Base,

результатов Intake,

Validation,

Governance,

Security.

KM-6 является финальным арбитром решений, но не источником истины.

❗ Решение без обоснования считается недействительным.

2. Область применения
Стандарт обязателен для:

всех автоматических решений,

всех agent-driven действий,

всех операций promotion / rejection знаний,

всех ситуаций с повышенным риском.

Нарушение стандарта = BLOCK.

3. Принципы принятия решений (НЕ ОБСУЖДАЮТСЯ)
Knowledge-Driven
Решения принимаются только на основе KB.

Multi-Option Reasoning
Всегда рассматривается ≥2 альтернатив.

Risk-Aware
Риск оценивается явно.

Explainable Decision
Решение должно быть объяснимо.

Human-Supremacy
Человек имеет право финального override.

4. Входные данные решения
KM-6 MUST использовать:

Candidate Knowledge

Validation Reports

Governance Policies

Security Signals

Contextual Constraints

Отсутствие входных данных = INSUFFICIENT_KNOWLEDGE.

5. Decision Flow (канонический)
scss
Копировать код
Intent
 → Context Analysis
 → Constraint Identification
 → Option Generation (≥2)
 → Risk Scoring
 → Impact Assessment
 → Decision Selection
 → Justification
 → Logging
 → (Escalation if needed)
Отклонение от flow = INVALID DECISION.

6. Типы решений
Тип	Описание
APPROVE	Разрешить действие
REJECT	Отклонить
ESCALATE	Передать человеку
DEFER	Отложить до доп. данных
REQUIRE_MORE_INFO	Запросить данные

7. Risk Scoring Model
Каждое решение MUST иметь риск-оценку.

Пример:

yaml
Копировать код
risk_assessment:
  data_sensitivity: medium
  source_trust: low
  impact_scope: high
  reversibility: low
  total_risk: high
High Risk → ESCALATE.

8. Decision Justification (обязательна)
Каждое решение MUST иметь обоснование.

Пример:

yaml
Копировать код
decision_justification:
  decision: REJECT
  reason: "Conflict with NormGraph requirement X"
  references:
    - KB:LAW-152:REQ-12
    - ValidationReport:VR-2025-021
Без justification → INVALID.

9. Human Escalation Rules
Эскалация обязательна, если:

риск = high,

затрагивается governance,

затрагиваются нормативные знания,

обнаружен конфликт стандартов.

10. Logging & Traceability
Каждое решение MUST быть залогировано.

Логи включают:

intent

варианты

риск

финальное решение

justification

approver (если есть)

Хранение:

swift
Копировать код
knowledge_base/80_logs/
11. Ограничения KM-6
KM-6 НЕ МОЖЕТ:

менять стандарты,

обходить validation,

самоподтверждать high-risk решения,

действовать без логов.

12. Enforcement
KM-6 Decision Engine обязателен для всех агентов

GitHub Actions проверяют наличие стандартов

CODEOWNERS защищают decision-логику

13. Связанные стандарты
AI–KB Interaction Standard v1.0

Knowledge Intake Standard v1.0

Knowledge Validation Standard v1.0

Knowledge Governance Standard v1.0

Knowledge Security Standard v1.0

14. Заключение
KM-6 не думает “умнее”.
KM-6 думает “ответственнее”.

🔒 END OF STANDARD
