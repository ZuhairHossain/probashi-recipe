# 👵🏽 Dadi's Probashi Kitchen

A locally-run AI assistant built for the **Hacktoberfest 2026 DEV Weekend Challenge: Build for a Friend**. 

## The Story
My friend Nafis recently moved from Bangladesh to Melbourne, Australia. He has been incredibly homesick for authentic Bangladeshi food like *Kacchi Biryani* and *Shorshe Ilish*, but he struggles to find local ingredients in standard Aussie supermarkets and doesn't understand traditional vague measurements (like "ek mutho" / a handful).

This project solves that problem. "Dadi's Probashi Kitchen" acts as a warm, loving Bangladeshi grandmother. It takes traditional recipe requests, comforts the user in "Banglish," swaps hard-to-find ingredients for Western supermarket alternatives, and converts measurements into exact grams and cups.

## Why Open Source?
1. **Cultural Customization:** Using an open-weight model allowed me to heavily customize the system prompt to capture the exact warmth, vocabulary, and specific tone of a real South Asian grandmother, avoiding the robotic feel of closed models.
2. **Privacy & Cost:** Family recipes are sacred. By using **Google's Gemma 2B** via Ollama, the model is lightweight enough to run flawlessly on a local CPU. This means my friend can use it entirely offline, it costs $0 to host, and private data never touches a corporate cloud server.

## Tech Stack
* **Frontend:** Python & Streamlit
* **AI Engine:** Ollama (running locally)
* **Model:** Google Gemma (gemma2:2b) targeting the *Best Use of Gemma* prize category.

## How to Run Locally

1. **Install Ollama:** Download from [ollama.com](https://ollama.com/)
2. **Pull the Gemma model:**
3. **Clone this repository & setup environment:**

```bash
git clone https://github.com/ZuhairHossain/probashi-recipe.git
cd probashi-recipe
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. **Run the app:**
```bash
streamlit run app.py
```

5. **Open the app:**
Open [http://localhost:8501](http://localhost:8501) in your browser.