# gpt2_text_gen.py

import sys

# Check for transformers installation
try:
    from transformers import GPT2LMHeadModel, GPT2Tokenizer
except ImportError:
    print("❌ Transformers library not installed. Run: pip install transformers torch")
    sys.exit(1)

import torch

def load_model():
    """Load GPT-2 tokenizer and model."""
    try:
        tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        model = GPT2LMHeadModel.from_pretrained('gpt2')
        return tokenizer, model
    except Exception as e:
        print(f"❌ Error loading GPT-2 model: {e}")
        sys.exit(1)

def get_response(prompt, tokenizer, model, max_length=100):
    """Generate response from GPT-2."""
    try:
        inputs = tokenizer.encode(prompt, return_tensors='pt')
        outputs = model.generate(
            inputs,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,   # avoid repetitive text
            do_sample=True,
            top_k=50,
            top_p=0.95
        )
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
    except Exception as e:
        return f"❌ Error generating response: {e}"

def main():
    print("=== GPT-2 Text Generation on Windows ===\n")
    
    tokenizer, model = load_model()
    
    while True:
        print("\nOptions:")
        print("1. Question form")
        print("2. Command form")
        print("3. Exit")
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            prompt = input("Enter your question prompt: ")
            print("\nGenerating response...\n")
            print(get_response(prompt, tokenizer, model))
            
        elif choice == "2":
            prompt = input("Enter your command prompt: ")
            print("\nGenerating response...\n")
            print(get_response(prompt, tokenizer, model))
        
        elif choice == "3":
            print("Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
