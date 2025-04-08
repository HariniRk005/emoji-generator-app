import streamlit as st
from model.generator import generate_emoji
from PIL import Image

st.set_page_config(page_title="AI Emoji Generator", layout="centered")
st.title("🎨 AI Emoji Generator using NLP + GAN (Simulated)")
st.markdown("Describe a feeling, and the AI will generate a matching emoji!")

user_input = st.text_input("Enter a description (e.g., 'sleepy face', 'pizza love')")

if st.button("Generate Emoji"):
    with st.spinner("Generating emoji..."):
        emoji_path = generate_emoji(user_input)
        image = Image.open(emoji_path)
        st.image(image, caption=f"Emoji for: '{user_input}'", use_column_width=True)
