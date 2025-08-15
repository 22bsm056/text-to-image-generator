import os
from huggingface_hub import InferenceClient
import argparse

# Function to generate image from text prompt
def generate_image(prompt, api_key, model="black-forest-labs/FLUX.1-dev", output_file="generated_image.png"):
    """
    AI Agent: Takes a text prompt and generates an image using Hugging Face's free Inference API.
    """
    # Initialize the client with your API key
    client = InferenceClient(token=api_key)
    
    try:
        # Call the API to generate the image
        image = client.text_to_image(
            prompt=prompt,
            model=model
        )
        
        # Save the generated image
        image.save(output_file)
        print(f"Image generated and saved as '{output_file}'!")
    except Exception as e:
        print(f"Error generating image: {e}")

if __name__ == "__main__":
    # Parse command-line arguments for the text prompt
    parser = argparse.ArgumentParser(description="AI Agent for Text-to-Image Generation")
    parser.add_argument("prompt", type=str, help="Text prompt to generate an image from (e.g., 'A futuristic city at sunset')")
    parser.add_argument("--output", type=str, default="generated_image.png", help="Output file name for the image")
    
    args = parser.parse_args()
    
    # Set your Hugging Face API key (preferably via environment variable)
    api_key = os.getenv("HF_TOKEN", "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")  # Replace with your token if not using env variable
    
    generate_image(args.prompt, api_key, output_file=args.output)