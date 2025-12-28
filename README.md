# Bot-Trainer

A Natural Language Understanding (NLU) model trainer and evaluator for chatbots powered by Large Language Models (LLMs). This project provides a Streamlit-based web interface for testing intent classification, entity extraction, and evaluating model performance using the Groq API.

## What It Does

Bot-Trainer is an NLU system that processes user messages to understand their intent and extract relevant entities. It supports the following core functionalities:

### Intent Classification
Classifies user messages into predefined intent categories such as:
- `greet` - General greetings
- `book_flight` - Flight booking requests
- `order_food` - Food ordering
- `cancel_booking` - Cancellation requests
- `check_weather` - Weather inquiries
- `track_order` - Order tracking
- `set_reminder` - Reminder creation
- `play_music` - Music playback requests
- `book_hotel` - Hotel reservations
- `currency_convert` - Currency conversion

### Entity Extraction
Extracts relevant entities from user input such as:
- Locations (cities, destinations)
- Dates and times
- Food items
- Song names and artists

### Model Evaluation
Provides comprehensive model evaluation capabilities including:
- Accuracy, Precision, Recall, and F1-Score metrics
- Confusion matrix visualization
- CSV-based batch evaluation

## How It Works

### Architecture

The system uses a prompt-based approach with LLMs to perform NLU tasks:

1. **User Input Processing**: User messages are received through the Streamlit interface
2. **LLM Inference**: Messages are sent to the Groq API with carefully crafted prompts
3. **Intent Classification**: The LLM predicts the intent and confidence score from predefined categories
4. **Entity Extraction**: The LLM extracts entities present in the text using open-vocabulary extraction
5. **Response Generation**: Results are displayed in the UI with confidence scores and extracted entities

### Prompt Engineering

The system uses specialized prompt templates:
- **Intent Prompt**: Constrains the LLM to choose from valid intent categories only
- **Entity Prompt**: Instructs the LLM to extract only entities present in the text without hallucination

### Evaluation Pipeline

For model evaluation:
1. Upload a CSV file with `text` and `label` columns
2. The system processes each row through the intent classifier
3. Predictions are compared against ground truth labels
4. Metrics are computed using scikit-learn
5. Results are visualized with confusion matrix heatmaps

## Tech Stack

- **Python** - Primary programming language
- **Streamlit** - Web application framework for the UI
- **Groq API** - LLM inference provider (using Llama 3.1 8B Instant model)

### Data Processing & Model Evaluation 
- **scikit-learn** - Evaluation metrics and confusion matrix
- **pandas** - Data manipulation and CSV processing
- **numpy** - Numerical operations

### Visualization
- **matplotlib** - Plotting framework
- **seaborn** - Statistical data visualization

### Utilities
- **python-dotenv** - Environment variable management
- **logging** - Application logging

## Project Structure

```
Bot- Trainer/
├── app.py                          # Main Streamlit application entry point
├── requirements.txt                # libraries required
├── .env                            # Environment variables (API keys)
├── .gitignore                      # Git ignore file
├── logs/                           # logs
│   └── bot_trainer.log             
└── src/                            
    ├── config/                     
    │   └── settings.py             # Settings and environment configuration
    ├── data/                       
    │   ├── dataset_loader.py       # Intent dataset loader
    │   └── intents.json            # Intent definitions and examples
    ├── evaluation/                 
    │   └── evaluator.py            # Metrics computation and normalization
    ├── llm/                        
    │   ├── llm_interface.py        # Groq API client and LLM calls
    │   └── prompt_templates.py     # Prompt engineering templates
    ├── nlu/                        
    │   ├── intent_classifier.py    # Intent classification logic
    │   └── entity_extractor.py     # Entity extraction logic
    └── utils/                      
        └── logger.py               # Logging configuration                       
```

## Installation

### Prerequisites
- Python 3.8 or higher
- Groq API key (sign up at [https://groq.com](https://groq.com))

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/Swayam-S-Bora/bottrainer-nlu-llm.git
cd bottrainer-nlu-llm
```

2. **Create a virtual environment**
```bash
python -m venv venv
```

3. **Activate the virtual environment**

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Configure environment variables**

Create a `.env` file in the root directory with the following content:
```
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=llama-3.1-8b-instant
```

Replace `your_groq_api_key_here` with your actual Groq API key.

6. **Run the application**
```bash
streamlit run app.py
```

7. **Access the application**

The application will open in your default browser at `http://localhost:8501`

## Usage

### Testing the Model

1. Navigate to the "Test Model" tab
2. Enter a message in the text input field
3. Click "Analyze" to see the predicted intent and extracted entities
4. View confidence scores and entity details
5. Expand "See raw JSON output" for the complete API response

### Evaluating the Model

1. Navigate to the "Evaluation" tab
2. Prepare a CSV file with two columns: `text` and `label`
3. Upload the CSV file using the file uploader
4. Wait for the evaluation to complete
5. View accuracy, precision, recall, and F1-score metrics
6. Analyze the confusion matrix to identify misclassifications

## Logging

Application logs are stored in the `logs/bot_trainer.log` file with the following information:
- Timestamp of each operation
- Log level (INFO, DEBUG, ERROR)
- Module name
- Log message

Logs include user inputs, LLM responses, and error traces for debugging.