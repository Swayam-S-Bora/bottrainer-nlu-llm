from src.llm.llm_interface import predict_intent
from src.utils.logger import get_logger

logger = get_logger("IntentClassifier")

def classify_intent(text: str):
    logger.info(f"Classifying intent for text: {text}")

    result = predict_intent(text)

    logger.info(
        f"Predicted intent={result.get('intent')} "
        f"confidence={result.get('confidence')}"
    )

    return {
        "intent": result.get("intent", "unknown"),
        "confidence": result.get("confidence", 0.0)
    }
