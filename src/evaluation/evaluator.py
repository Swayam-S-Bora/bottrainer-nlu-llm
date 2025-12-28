from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    confusion_matrix
)

VALID_INTENTS = {
    "greet",
    "book_flight",
    "order_food",
    "cancel_booking",
    "check_weather",
    "track_order",
    "set_reminder",
    "play_music",
    "book_hotel",
    "currency_convert"
}

def normalize(label: str) -> str:
    """
    Normalize intent strings so that variants like:
    'Book Flight', 'book_flight-', 'book flight'

    all map to:
    'book_flight'
    """

    if label is None:
        return "unknown"

    label = (
        str(label)
        .strip()
        .lower()
        .replace("-", "_")
        .replace(" ", "_")
        .replace("__", "_")
    )

    return label

def clean_prediction(label: str) -> str:

    label = normalize(label)

    if label in VALID_INTENTS:
        return label

    # fallback for invalid LLM outputs
    return "unknown"

def evaluate(y_true_raw, y_pred_raw):
    """
    y_true_raw : list of ground truth labels (strings)
    y_pred_raw : list of predicted labels from model
    """

    # normalize true labels
    y_true = [normalize(x) for x in y_true_raw]

    # clean predictions to valid ontology
    y_pred = [clean_prediction(x) for x in y_pred_raw]

    all_labels = sorted(list(VALID_INTENTS))

    # build confusion matrix over valid labels only
    cm = confusion_matrix(
        y_true,
        y_pred,
        labels=all_labels
    )

    # compute metrics
    accuracy = accuracy_score(y_true, y_pred)

    precision, recall, f1, _ = precision_recall_fscore_support(
        y_true,
        y_pred,
        labels=all_labels,
        average="weighted",
        zero_division=0
    )

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "confusion_matrix": cm,
        "labels": all_labels,
    }
