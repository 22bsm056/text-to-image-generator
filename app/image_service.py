import os
from huggingface_hub import InferenceClient
from PIL import Image
from io import BytesIO

def generate_image(prompt: str, output_file: str = "generated_image.png") -> str:
    """
    Generates an image from a text prompt using Hugging Face Inference API.
    """
    api_key = os.getenv("HF_TOKEN", "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")  # Replace if not using env variable
    client = InferenceClient(token=api_key)

    try:
        image = client.text_to_image(
            prompt=prompt,
            model="Qwen/Qwen-Image"
        )

        image.save(output_file)
        return output_file
    except Exception as e:
        raise RuntimeError(f"Error generating image: {e}")
