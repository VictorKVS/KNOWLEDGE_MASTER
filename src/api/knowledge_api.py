#8️⃣ API layer (будущий сервис)
#📄 src/api/knowledge_api.py

from adapters.ai_adapter import AIAdapter


def process_knowledge_request(item, risk_level="low"):
    adapter = AIAdapter()
    return adapter.handle_request(item, risk_level