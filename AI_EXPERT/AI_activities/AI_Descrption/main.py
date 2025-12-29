# blip_caption.py
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

def caption_single_image(image_path="test.jpg"):
    """
    Captions a single local image using BLIP.
    """
    try:
        # Load image
        image = Image.open(image_path).convert("RGB")
    except Exception as e:
        print(f"Could not load image '{image_path}'. Error: {e}")
        return

    # Load BLIP model and processor (will cache locally)
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    # Prepare inputs
    inputs = processor(images=image, return_tensors="pt")

    # Generate caption
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)

    print("Image:", image_path)
    print("Caption:", caption)

def main():
    caption_single_image()

if __name__ == "__main__":
    main()
