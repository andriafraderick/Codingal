# main.py
from diffusers import StableDiffusionInpaintPipeline
import torch
from PIL import Image, ImageEnhance, ImageFilter
import os

# Load inpainting model on CPU
pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "runwayml/stable-diffusion-inpainting",
    torch_dtype=torch.float32  # CPU uses float32
)
pipe = pipe.to("cpu")  # Use CPU

def generate_inpainting_image(prompt, image_path, mask_path):
    """Generates inpainted image from base image, mask, and prompt."""
    init_image = Image.open(image_path).convert("RGB")
    mask_image = Image.open(mask_path).convert("RGB")
    result = pipe(prompt=prompt, image=init_image, mask_image=mask_image).images[0]
    return result

def post_process_image(image):
    """Applies brightness, contrast, and Gaussian blur."""
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.2)  # +20% brightness
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.3)  # +30% contrast
    image = image.filter(ImageFilter.GaussianBlur(radius=2))  # soft-focus
    return image

def main():
    print("Welcome to the Inpainting and Post-Processing Workshop!")
    print("Type 'exit' at any prompt to quit.\n")

    while True:
        prompt = input("Enter a description for the inpainting (or 'exit' to quit):\n")
        if prompt.lower() == "exit":
            print("Goodbye!")
            break

        image_path = input("Enter the path to the base image (e.g., base.png):\n")
        if image_path.lower() == "exit":
            break
        if not os.path.exists(image_path):
            print(f"❌ File not found: {image_path}\n")
            continue

        mask_path = input("Enter the path to the mask image (e.g., mask.png):\n")
        if mask_path.lower() == "exit":
            break
        if not os.path.exists(mask_path):
            print(f"❌ File not found: {mask_path}\n")
            continue

        try:
            print("\nGenerating inpainted image... This may take a few minutes on CPU.")
            inpainted = generate_inpainting_image(prompt, image_path, mask_path)

            print("Applying post-processing effects...")
            processed = post_process_image(inpainted)

            processed.show()

            save_option = input("Do you want to save the processed image? (yes/no): ").strip().lower()
            if save_option == "yes":
                file_name = input("Enter a name for the image file (without extension): ").strip() or "inpainted_image"
                file_name = "".join(c for c in file_name if c.isalnum() or c in ("_", "-")).rstrip()
                processed.save(f"{file_name}.png")
                print(f"✅ Image saved as {file_name}.png\n")

            print("-" * 80 + "\n")

        except Exception as e:
            print(f"❌ An error occurred: {e}\n")

if __name__ == "__main__":
    main()
