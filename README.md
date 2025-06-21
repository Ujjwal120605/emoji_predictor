# emoji_predictor# 🤖 Emoji Prediction App 🎉

This is a Streamlit-powered web app that predicts an appropriate emoji based on the input tweet or message text. It uses a machine learning model trained on a dataset of tweets labeled with emojis.

---

## 📌 Project Structure


---

## 🔮 How It Works

- `Train.csv` contains tweet-like messages labeled with numeric emoji IDs.
- `Mapping.csv` maps those numeric IDs to actual emojis.
- The model is trained using TF-IDF vectorization + Logistic Regression.
- Users input a message via Streamlit, and the model returns a predicted emoji.

---

# 🤖 Emoji Prediction App 🎉

This is a Streamlit-powered web app that predicts an appropriate emoji based on the input tweet or message text.

🌐 **Live Demo**: [Click here to try the app][(https://your-username-your-app-name.streamlit.app) ](http://localhost:8505/) 
_(Replace with your actual URL once deployed)_

---

## 📌 Project Structure
...


### 1️⃣ Clone the repo or download the files.

### 2️⃣ Set up a virtual environment (recommended)

```bash
cd emoji
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
