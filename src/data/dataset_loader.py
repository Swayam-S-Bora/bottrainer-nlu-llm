import json
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "intents.json")

def load_intents():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

def get_training_examples():
    data = load_intents()
    
    examples = []
    labels = []

    for item in data["intents"]:
        for ex in item["examples"]:
            examples.append(ex)
            labels.append(item["name"])

    return examples, labels
