AI–KB Interaction Standard v1.0

(Официальный стандарт взаимодействия ИИ с Базой Знаний)

1. Назначение стандарта

AI–KB Interaction Standard определяет ЕДИНСТВЕННЫЙ допустимый способ, которым:

внутренние ИИ,

внешние ИИ,

агентные системы,

федеративные KB

могут читать из KB и предлагать изменения в KB.

❗ Прямой доступ ИИ к KB запрещён.

2. Базовые принципы (не обсуждаются)

Zero Trust AI
Любой ИИ = недоверенный источник по умолчанию.

KB is Source of Truth
ИИ никогда не является источником истины.

Contract-Based Interaction
Любое взаимодействие — только через контракт.

Deny-by-Default
Всё запрещено, пока явно не разрешено.

Human-in-the-loop для критичных зон

3. Классы взаимодействия
Тип ИИ	Роль	Права
Internal AI	Агенты MindForge	Read + Propose
External AI	API / подрядчики	Propose only
Federated KB	Партнёрские KB	Exchange via contract
Human	Governor	Approve / Reject
4. Допустимые операции
Операция	Разрешение
Read KB	Через Read View
Propose Knowledge	Через Intake Contract
Modify KB	❌ запрещено
Modify Ontology	❌ запрещено
Delete Knowledge	❌ запрещено
5. Канонический поток взаимодействия
AI
 → AI Adapter
 → Knowledge Intake Contract
 → Validation Pipeline
 → KM-6 Decision Engine
 → (Human Approval, if needed)
 → Versioned KB Update
 → Audit Logs

6. Обязательные слои защиты

Security Filter (poisoning, injection)

Semantic Filter (ontology, terminology)

Consistency Filter (conflicts, NormGraph)

Governance Filter (trust, approval)

7. Обязательные артефакты стандарта
knowledge_base/
 ├── 30_intake/
 ├── 35_validation/
 ├── 80_logs/
 └── 90_interagent/


📌 Этот стандарт обязателен для всех ИИ.

🟩 ШАГ 2
Knowledge Intake Contract Pack

(машиночитаемые контракты приёма знаний)

2.1 Базовый контракт (шаблон)

KNOWLEDGE_INTAKE_CONTRACT.yaml

contract_id: KIC-EXT-LLM-001

source:
  type: external_ai
  id: gpt_vendor_x
  trust_level: low

permissions:
  read: false
  propose: true
  write: false

allowed_content:
  - summaries
  - extracted_facts
  - hypotheses

forbidden_content:
  - normative_statements
  - policy_changes
  - ontology_changes

validation:
  required:
    - security_check
    - semantic_check
    - consistency_check
    - human_review

storage:
  initial_zone: raw
  promotion_allowed: false

logging:
  level: full

2.2 Контракт для Internal AI
contract_id: KIC-INT-AGENT-002

source:
  type: internal_ai
  role: rag_agent
  trust_level: medium

permissions:
  read: true
  propose: true
  write: false

allowed_content:
  - chunk_annotations
  - candidate_embeddings
  - retrieval_metadata

validation:
  required:
    - semantic_check
    - governance_check

approval_required: km6

2.3 Контракт для Federation KB ↔ KB
contract_id: KIC-FED-KB-001

source:
  type: federated_kb
  organization: partner_x

exchange:
  mode: facts_and_graphs
  allowed_layers:
    - semantic
    - graph

constraints:
  - no_raw_documents
  - no_personal_data

trust_mapping:
  local_trust: medium

2.4 Где хранятся контракты
knowledge_base/30_intake/intake_contracts/
 ├── external_ai.yaml
 ├── internal_agents.yaml
 └── federation.yaml

🟨 ШАГ 3
End-to-End сценарий (рабочий контур)
Сценарий:

External AI → KB → RAG → Ответ

Шаг 1. Внешний ИИ предлагает знание
External LLM
 → summary / extracted facts


❗ Не ответ, а кандидат знания.

Шаг 2. Intake Contract

проверка прав

запись в raw/

фиксация источника

Шаг 3. Validation Pipeline

Security Agent → риск

Semantic Agent → термины

Graph Agent → конфликты

KM-6 → решение

Шаг 4. Approval

если риск > threshold → человек

иначе → версия KB обновляется

Шаг 5. RAG Retrieval
User Query
 → Hybrid Retrieval
 → Graph Subset
 → Context Assembly
 → LLaMA (controlled)

Шаг 6. Ответ

Ответ содержит:

факты

ссылки на KB

ограничения

уровень доверия

🔒 КЛЮЧЕВАЯ ФИКСАЦИЯ (как специалист)

ИИ не обновляет знания.
ИИ предлагает кандидатов.
KB решает.
Человек несёт ответственность.