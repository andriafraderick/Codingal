from transformers import BlipProcessor, BlipForConditionalGeneration, AutoTokenizer, AutoModelForCausalLM
from PIL import Image
import torch
import os

# Load BLIP model + processor (for image captioning)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load a text generation model (can be small / fast)
tok = AutoTokenizer.from_pretrained("gpt2")
text_model = AutoModelForCausalLM.from_pretrained("gpt2")

def generate_caption(image_path):
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    out = blip_model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

def generate_text_from_prompt(prompt, max_length=100):
    inputs = tok(prompt, return_tensors="pt")
    outputs = text_model.generate(**inputs, max_length=max_length)
    text = tok.decode(outputs[0], skip_special_tokens=True)
    return text

def truncate_words(text, count):
    words = text.strip().split()
    return " ".join(words[:count])

def main():
    image_path = input("Enter path to image (e.g., test.jpg): ").strip()
    if not os.path.exists(image_path):
        print("❌ File not found!")
        return

    print("\n🖼️ Generating caption…")
    caption = generate_caption(image_path)
    print(f"📝 Caption: {caption}")

    # Description (30 words)
    prompt_desc = f"Write a 30-word detailed description of: {caption}"
    full_desc = generate_text_from_prompt(prompt_desc, max_length=100)
    desc30 = truncate_words(full_desc, 30)
    print(f"\n📘 Description (30 words): {desc30}")

    # Summary (50 words)
    prompt_sum = f"Write a 50-word summary of: {caption}"
    full_summary = generate_text_from_prompt(prompt_sum, max_length=120)
    sum50 = truncate_words(full_summary, 50)
    print(f"\n📚 Summary (50 words): {sum50}")

if __name__ == "__main__":
    main()
