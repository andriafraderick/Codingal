import requests

# Correct API endpoint (random fact)
url = "https://uselessfacts.jsph.pl/random.json?language=en"

# Function to fetch and display a random fact
def get_random_fact():
    response = requests.get(url)

    if response.status_code == 200:
        fact_data = response.json()
        print(f"\n💡 Did you know?\n{fact_data['text']}\n")
    else:
        print("❌ Failed to fetch fact")

# Main loop
print("📚 Random Facts Generator")
print("Press Enter to get a fact or type 'q' to quit")

while True:
    user_input = input(">> ")
    if user_input.lower() == 'q':
        print("Goodbye 👋")
        break
    get_random_fact()
