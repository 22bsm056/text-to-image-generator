import os
import requests
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
from datetime import datetime

# Load API key
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")
HF_MODEL = "runwayml/stable-diffusion-v1-5"  # works without license approval

st.title("🖼 Text-to-Image Generator (Hugging Face)")

prompt = st.text_input("Enter your prompt:", placeholder="e.g., A futuristic city skyline at sunset")

if st.button("Generate Image"):
    if not prompt.strip():
        st.error("Please enter a prompt.")
    else:
        with st.spinner("Generating image..."):
            try:
                response = requests.post(
                    f"https://api-inference.huggingface.co/models/{HF_MODEL}",
                    headers={"Authorization": f"Bearer {HF_API_KEY}"},
                    json={"inputs": prompt}
                )

                if response.status_code != 200:
                    st.error(f"API Error {response.status_code}: {response.text}")
                else:
                    image = Image.open(BytesIO(response.content))
                    filename = f"generated_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                    image.save(filename)

                    st.image(image, caption="Generated Image", use_column_width=True)
                    st.success(f"Image saved as {filename}")

            except Exception as e:
                st.error(f"Error generating image: {e}")
