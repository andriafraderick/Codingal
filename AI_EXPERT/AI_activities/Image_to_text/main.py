from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from colorama import init, Fore, Style
import torch
import os

# Initialize colorama
init(autoreset=True)

# Load BLIP model locally
print(Fore.YELLOW + "🔄 Loading BLIP model (first time may take a minute)...")
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

def generate_caption(image):
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs, max_new_tokens=40)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

def truncate_text(text, words):
    return " ".join(text.split()[:words])

def print_menu():
    print(f"""{Style.BRIGHT}
{Fore.GREEN}================ Image-to-Text Conversion =================
1. Caption (5 words)
2. Description (30 words)
3. Summary (50 words)
4. Exit
===============================================================
""")

def main():
    image_path = input(
        Fore.BLUE + "Enter the path of the image (e.g., test.jpg): "
    )

    if not os.path.exists(image_path):
        print(Fore.RED + "❌ Image file not found.")
        return

    image = Image.open(image_path).convert("RGB")

    caption = generate_caption(image)
    print(Fore.YELLOW + f"\n📝 Basic caption: {Style.BRIGHT}{caption}\n")

    while True:
        print_menu()
        choice = input(Fore.CYAN + "Enter your choice (1-4): ")

        if choice == "1":
            print(Fore.GREEN + "✅ Caption (5 words):",
                  truncate_text(caption, 5))

        elif choice == "2":
            print(Fore.GREEN + "✅ Description (30 words):",
                  truncate_text(caption, 30))

        elif choice == "3":
            print(Fore.GREEN + "✅ Summary (50 words):",
                  truncate_text(caption, 50))

        elif choice == "4":
            print(Fore.GREEN + "👋 Goodbye!")
            break

        else:
            print(Fore.RED + "❌ Invalid choice.")

if __name__ == "__main__":
    main()
