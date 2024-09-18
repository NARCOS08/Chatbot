import random

# Define a set of responses for the chatbot
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm doing well, thanks for asking!", "I'm just a program, but I'm good!", "Doing great, how about you?", "im doing great"],
    "what is your name": ["I'm a chatbot created to assist you.", "You can call me ChatBot.", "My name is ChatBot!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["I'm sorry, I don't understand that.", "Can you rephrase?", "I'm not sure how to respond to that."]
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()

    # Find a matching response or use a default response
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Main function to run the chatbot
def chatbot():
    print("ChatBot: Hi! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye!")
            break
        else:
            response = get_response(user_input)
            print(f"ChatBot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
