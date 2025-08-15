import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from PIL import Image

# Load variables from .env file into environment
load_dotenv()

def generate_image(prompt: str, output_file: str = "generated_image.png") -> str:
    api_key = os.getenv("HF_TOKEN")
    if not api_key:
        raise RuntimeError("HF_TOKEN not found in environment or .env file")

    client = InferenceClient(token=api_key)

    try:
        image = client.text_to_image(
            prompt=prompt,
            model="Qwen/Qwen-Image"  # use free model
        )
        image.save(output_file)
        return output_file
    except Exception as e:
        raise RuntimeError(f"Error generating image: {e}")
