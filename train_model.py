import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load training data
df = pd.read_csv("Train.csv")

# Basic tweet cleaning
def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#", "", text)
    return text.lower().strip()

df['cleaned'] = df['TEXT'].apply(clean_text)

# Vectorization
vectorizer = TfidfVectorizer(max_features=8000, ngram_range=(1, 2))
X = vectorizer.fit_transform(df['cleaned'])
y = df['Label']

# Train model
model = LogisticRegression(class_weight='balanced', max_iter=1500)
model.fit(X, y)

# Save model
joblib.dump((model, vectorizer), "emoji_model.pkl")
print("✅ Improved model trained and saved")

