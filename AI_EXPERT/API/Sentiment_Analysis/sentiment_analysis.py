from transformers import pipeline

# Load sentiment analysis model locally
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

text_input = input("Enter text for sentiment analysis: ")

result = classifier(text_input)

print(f"Sentiment: {result[0]['label']}")
print(f"Confidence: {result[0]['score']:.2f}")
