import streamlit as st
import joblib
import pandas as pd

# Load emoji mapping
mapping_df = pd.read_csv("Mapping.csv")

id_to_emoji = dict(zip(mapping_df['number'], mapping_df['emoticons']))

# Load model
try:
    model, vectorizer = joblib.load("emoji_model.pkl")
except:
    st.error("❌ Run train_model.py first to create emoji_model.pkl")
    st.stop()

st.set_page_config(page_title="Emoji Predictor 🤖", page_icon="✨")
st.title("🔮 Emoji Predictor from Tweet Text")

# Input box
text = st.text_area("Enter a tweet or message:")

if text:
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    emoji = id_to_emoji.get(prediction, "❓")
    
    st.subheader("Predicted Emoji:")
    st.markdown(f"<h1 style='font-size:64px'>{emoji}</h1>", unsafe_allow_html=True)
