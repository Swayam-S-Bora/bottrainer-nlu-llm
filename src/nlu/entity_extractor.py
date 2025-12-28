from src.llm.llm_interface import extract_entities
from src.data.dataset_loader import load_intents
from src.utils.logger import get_logger
logger = get_logger("EntityExtractor")

def get_all_entities():
    data = load_intents()

    entities_section = data.get("entities", {})

    # flatten all entity VALUES (Delhi, pizza, etc.)
    values = []

    for entity_type, entity_values in entities_section.items():
        values.extend(entity_values)

    return values

def get_entities(text: str):
    logger.info(f"Extracting entities for text: {text}")

    # direct open-vocabulary extraction
    result = extract_entities(
        text=text,
        entity_list=[]  # no restriction list
    )

    entities = result.get("entities", {})

    # remove blanks/nulls
    clean = {}
    for k, v in entities.items():
        if v is not None and str(v).strip() != "":
            clean[k] = v

    logger.info(f"Extracted entities: {clean}")

    return clean



DATE_KEYWORDS = [
    "today",
    "tomorrow",
    "yesterday",
    "next week",
    "next month",
    "this week",
    "this month",
    "tonight",
    "this weekend"
]

def find_dates(text: str):
    found = []

    text_lower = text.lower()
    for w in DATE_KEYWORDS:
        if w in text_lower:
            found.append(w)

    return found

