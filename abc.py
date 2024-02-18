import random

# Define some responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm doing well, thank you!", "I'm great, thanks for asking!"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm not sure how to respond to that.", "Could you please rephrase that?", "Sorry, I didn't understand."],
}

# Function to get a response to a user input
def get_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])

# Main function to handle the conversation
def main():
    print("Welcome to the Simple Chatbot!")
    print("You can start chatting. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        response = get_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
