from groq import Groq
import json
from streamlit import text
from src.config.settings import settings
from src.llm.prompt_templates import INTENT_PROMPT, ENTITY_PROMPT
from src.utils.logger import get_logger
from src.evaluation.evaluator import VALID_INTENTS

logger = get_logger(__name__)

# Initialize Groq client
client = Groq(api_key=settings.GROQ_API_KEY)

def ask_llm(prompt: str):
    logger.info("Sending prompt to LLM")

    try:
        completion = client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        content = completion.choices[0].message.content

        logger.debug(f"LLM raw response: {content}")

        try:
            parsed = json.loads(content)
            logger.info("LLM JSON parsed successfully")
            return parsed

        except json.JSONDecodeError:
            logger.error("Failed to parse JSON from LLM")
            return {"error": "Invalid JSON returned", "raw_output": content}

    except Exception as e:
        logger.exception("Error while calling LLM")
        return {"error": str(e)}


def predict_intent(text: str):
    prompt = INTENT_PROMPT.format(
    text=text,
    valid_intents=", ".join(sorted(VALID_INTENTS))
)
    return ask_llm(prompt)


def extract_entities(text: str, entity_list: list = None):
    if entity_list is None:
        entity_list = []

    prompt = ENTITY_PROMPT.format(text=text)

    return ask_llm(prompt)
