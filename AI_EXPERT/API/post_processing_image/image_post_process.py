import os
from huggingface_hub import InferenceClient
from PIL import Image, ImageEnhance, ImageFilter
from io import BytesIO
from config import HF_API_KEY

# Create a single InferenceClient instance
client = InferenceClient(api_key=HF_API_KEY)

def generate_image_from_text(prompt: str) -> Image.Image:
    """
    Generate image using the HF InferenceClient.text_to_image helper.
    """
    # You can try different models; this one is recommended by HF docs:
    model_id = "black-forest-labs/FLUX.1-dev"

    image = client.text_to_image(
        prompt=prompt,
        model=model_id,
    )
    return image

def post_process_image(image: Image.Image) -> Image.Image:
    """
    Applies brightness, contrast, and a soft blur to the image.
    """
    # Brightness +20%
    enhancer = ImageEnhance.Brightness(image)
    bright_image = enhancer.enhance(1.2)

    # Contrast +30%
    enhancer = ImageEnhance.Contrast(bright_image)
    contrast_image = enhancer.enhance(1.3)

    # Soft-focus blur
    soft_focus_image = contrast_image.filter(ImageFilter.GaussianBlur(radius=2))
    return soft_focus_image

def main():
    print("Welcome to the Post‑Processing Magic Workshop!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter a description for the image (or 'exit' to quit):\n")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            print("\nGenerating image… (this may take a moment)…\n")
            image = generate_image_from_text(user_input)

            print("Applying post‑processing effects…\n")
            processed_image = post_process_image(image)

            processed_image.show()

            save_option = input("Do you want to save the processed image? (yes/no): ").strip().lower()
            if save_option == "yes":
                file_name = input("Enter a name for the image file (without extension): ").strip()
                processed_image.save(f"{file_name}.png")
                print(f"Image saved as {file_name}.png\n")

            print("-" * 80 + "\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    main()
