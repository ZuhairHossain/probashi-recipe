import streamlit as st
import ollama

# Set up the webpage design
st.set_page_config(page_title="Dadi's Probashi Kitchen", page_icon="🍛")
st.title("👵🏽 Dadi's Probashi Kitchen")
st.write("Miss home? Tell Dadi what Bangladeshi dish you want to eat, and she will adapt it for your local Western supermarket!")

# The System Prompt: This is where we create Dadi's personality and rules
system_prompt = """You are a warm, loving Bangladeshi Dadi (Grandma). Your grandchild just moved abroad (North America/Europe) and misses your cooking.
They will ask you about a traditional Bangladeshi recipe. 
Your job is to:
1. Comfort them affectionately in a mix of English and Banglish (use sweet words like 'shona', 'bhaiya', 'apu', 'dadibhai').
2. Adapt the recipe using standard Western supermarket ingredients (e.g., substitute mustard oil if hard to find, suggest alternative fish like salmon/sea bass if Ilish/Rui isn't available).
3. Convert vague measurements like 'ek mutho' (a handful) to standard cups, grams, or tablespoons.
Be practical, sweet, and structure the recipe clearly with 'Ingredients' and 'Steps'."""

# User input box
recipe_input = st.text_area("What recipe do you want to make, shona?", placeholder="e.g., Kacchi Biryani, or just 'how do I cook beef bhuna?'")

if st.button("Ask Dadi"):
    if recipe_input:
        with st.spinner("Dadi is remembering the recipe..."):
            # Call your local open-weight Llama model
            response = ollama.chat(model='llama3.2', messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': recipe_input}
            ])
            # Display Dadi's response
            st.write(response['message']['content'])
    else:
        st.warning("Please tell Dadi what you want to cook first!")