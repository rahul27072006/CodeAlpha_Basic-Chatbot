def chatbot():
    print("=" * 50)
    print("Welcome to the Basic Chatbot!")
    print("=" * 50)
    print("You can talk to me. Type 'bye' or 'exit' to end the chat.\n")
    while True:
        user_input = input("You: ").strip().lower()
        if not user_input:
            print("Bot: Please say something!\n")
            continue
        response = get_response(user_input)
        print(f"Bot: {response}\n")
        if user_input in ['bye', 'exit', 'goodbye', 'quit']:
            break
def get_response(user_input):
    if user_input in ['hello', 'hi', 'hey', 'greetings']:
        return "Hi! How can I help you today?"
    elif user_input in ['how are you', 'how are you?', 'how do you do']:
        return "I'm fine, thanks! How about you?"
    elif user_input in ['i am fine', 'i am good', 'im fine', 'im good', 'good', 'great']:
        return "That's great to hear!"
    elif user_input in ['what is your name', 'what is your name?', 'your name']:
        return "I'm a simple chatbot created for CodeAlpha!"
    elif user_input in ['help', 'what can you do', 'what can you do?']:
        return "I can chat with you! Try saying hello, asking how I am, or say bye to exit."
    elif user_input in ['thank you', 'thanks', 'thank you!', 'thanks!']:
        return "You're welcome! Happy to help!"
    elif user_input in ['bye', 'goodbye', 'exit', 'quit']:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that. Try saying 'hello', 'how are you', or 'bye'."
if __name__ == "__main__":
    chatbot()
