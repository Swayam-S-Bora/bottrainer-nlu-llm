INTENT_PROMPT = """
You are an intent classifier.

Allowed intents are ONLY:
{valid_intents}

Choose the **best matching** intent.
Do NOT answer unknown.
Do NOT invent new labels.

Return JSON only:

{{
 "intent": "<one of allowed intents>",
 "confidence": 0.0
}}

User: "{text}"
"""

ENTITY_PROMPT = """
You are an entity extraction model.

Extract ONLY the entities that are actually present in the text.
Do NOT include any entity if it is missing or not relevant.

Return STRICT JSON in this format:
{{
 "entities": {{
    "entity_type": "value"
 }}
}}

Rules:
- include only entities that appear in the text
- do not include empty strings
- do not invent values
- do not output keys with empty values

User message: "{text}"
"""
