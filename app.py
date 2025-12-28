import streamlit as st
from src.nlu.intent_classifier import classify_intent
from src.nlu.entity_extractor import get_entities
from src.evaluation.evaluator import evaluate
from src.utils.logger import get_logger

logger = get_logger("StreamlitApp")

st.set_page_config(page_title="BotTrainer NLU", page_icon="🤖")

st.title("🤖 BotTrainer")
st.subheader("LLM-Based NLU Model Trainer & Evaluator for Chatbots")
tabs = st.tabs(["Test Model", "Evaluation"])

st.markdown("---")

with tabs[0]:
    st.subheader("Test the NLU Model")

    user_input = st.text_input("Your message", placeholder="Type your message here...")

    analyze = st.button("Analyze")

    if analyze and user_input.strip():

        logger.info(f"User input: {user_input}")

        with st.spinner("Analyzing..."):

            intent_result = classify_intent(user_input)
            entities = get_entities(user_input)

        st.markdown("#### Predicted Intent")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(label="Intent", value=intent_result.get("intent", "unknown"))

        with col2:
            st.metric(label="Confidence", value=round(intent_result.get("confidence", 0.0), 3))

        st.markdown("#### Extracted Entities")

        if entities:
            for k, v in entities.items():
                st.write(f"• **{k}** → `{v}`")
        else:
            st.info("No entities detected.")

        st.markdown("---")

        with st.expander("See raw JSON output"):
            st.json(
                {
                    "intent": intent_result,
                    "entities": entities
                }
            )

    elif analyze:
        st.warning("Please enter a message first")


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with tabs[1]:

    st.subheader("Model Evaluation")

    st.write("Upload a CSV file with columns: **text**, **label**")

    uploaded = st.file_uploader("Upload evaluation dataset", type=["csv"])

    if uploaded is not None:

        df = pd.read_csv(uploaded)

        if "text" not in df.columns or "label" not in df.columns:
            st.error("CSV must contain 'text' and 'label' columns.")
        else:
            st.success("File loaded successfully")

            true_labels = []
            pred_labels = []

            progress = st.progress(0)

            for i, row in df.iterrows():
                text = row["text"]
                true = row["label"]

                pred = classify_intent(text)["intent"]

                true_labels.append(true)
                pred_labels.append(pred)

                progress.progress((i + 1) / len(df))

            results = evaluate(true_labels, pred_labels)

            st.markdown("#### Evaluation Metrics")

            st.write(f"**Accuracy:** {results['accuracy']:.3f}")
            st.write(f"**Precision:** {results['precision']:.3f}")
            st.write(f"**Recall:** {results['recall']:.3f}")
            st.write(f"**F1 Score:** {results['f1']:.3f}")

            st.markdown("#### Confusion Matrix")

            cm = results["confusion_matrix"]
            labels = results["labels"]

            fig, ax = plt.subplots(figsize=(10, 8))

            sns.heatmap(
                cm,
                annot=True,
                fmt="d",
                cmap="Blues",
                xticklabels=labels,
                yticklabels=labels,
                ax=ax
            )

            ax.set_title("Confusion Matrix")
            ax.set_xlabel("Predicted")
            ax.set_ylabel("Actual")

            # Improve readability of axis labels
            plt.xticks(rotation=45, ha="right")
            plt.yticks(rotation=0)

            st.pyplot(fig)
