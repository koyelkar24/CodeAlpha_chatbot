def chatbot():
    """
    A simple rule-based chatbot that responds to user input
    """       
    print("=" * 50)
    print("🤖 Welcome to Simple Chatbot!")
    print("I can respond to: hello, how are you, what's your name, bye")
    print("Type 'bye' to exit the chat")
    print("=" * 50)
    
    # Main chat loop
    while True:
        # Get user input and convert to lowercase for easier matching
        user_input = input("\nYou: ").lower().strip()
        
        # Rule 1: Greetig
        if user_input in ['hello', 'hi', 'hey', 'hola']:
            print("Bot: Hello! Nice to meet you! 👋")
        
        # Rule 2: How are you
        elif user_input in ['how are you', 'how are you?', 'how do you do']:
            print("Bot: I'm doing great, thank you for asking! 😊")
            print("Bot: How are you feeling today?")
        
        # Rule 3: Ask about bot's name
        elif user_input in ['what is your name', 'what\'s your name', 'who are you']:
            print("Bot: I'm SimpleBot, your friendly chatbot assistant! 🤖")
        
        # Rule 4: Thanks
        elif user_input in ['thanks', 'thank you', 'thank you!']:
            print("Bot: You're welcome! Happy to help! 🌟")
        
        # Rule 5: Goodbye - this will break the loop
        elif user_input in ['bye', 'goodbye', 'exit', 'quit', 'see you']:
            print("Bot: Goodbye! Thanks for chatting with me! 👋")
            print("Bot: Have a wonderful day! 🌈")
            break
        
        # Rule 6: Ask what the bot can do
        elif user_input in ['what can you do', 'help', 'options']:
            print("Bot: I can have simple conversations with you!")
            print("Bot: Try asking me: hello, how are you, what's your name, or say bye to exit.")
        
        # Rule 7: Default response for unknown inputs
        else:
            print("Bot: I'm still learning! I understand simple greetings like 'hello' or 'how are you?'")
            print("Bot: Try saying 'hello' or ask me 'what can you do?'")

# Advanced version with more features
def advanced_chatbot():
    """
    A more advanced version with additional features
    """
    print("=" * 50)
    print("🤖 Welcome to Advanced Chatbot!")
    print("I can: tell time, calculate, and have better conversations!")
    print("Type 'bye' to exit")
    print("=" * 50)
    
    import datetime
    chat_count = 0
    
    while True:
        user_input = input("\nYou: ").lower().strip()
        chat_count += 1
        
        # Enhanced greeting with context
        if any(word in user_input for word in ['hello', 'hi', 'hey']):
            if chat_count == 1:
                print("Bot: Hello! First time chatting with you! 👋")
            else:
                print("Bot: Hello again! Good to see you! 😊")
        
        # Feelings check
        elif 'how are you' in user_input:
            print("Bot: I'm functioning perfectly! Thanks for asking! ⚡")
            print("Bot: As a bot, I don't have feelings, but I'm here to help!")
        
        # Time request
        elif 'time' in user_input:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Bot: The current time is {current_time} ⏰")
        
        # Date request
        elif 'date' in user_input or 'today' in user_input:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            print(f"Bot: Today's date is {current_date} 📅")
        
        # Simple math calculation
        elif 'calculate' in user_input or 'what is' in user_input and '+' in user_input:
            try:
                # Extract numbers and calculate
                parts = user_input.split('+')
                if len(parts) == 2:
                    num1 = float(parts[0].strip())
                    num2 = float(parts[1].strip())
                    result = num1 + num2
                    print(f"Bot: {num1} + {num2} = {result} 🧮")
            except:
                print("Bot: I can help with simple addition like 'calculate 5+3'")
        
        # Bot information
        elif 'your name' in user_input:
            print("Bot: I'm AdvancedBot 1.0! 🤖")
            print("Bot: I'm here to assist you with various tasks!")
        
        # Goodbye
        elif any(word in user_input for word in ['bye', 'goodbye', 'exit']):
            print(f"Bot: Thanks for our {chat_count} message conversation! 👋")
            print("Bot: Hope to chat with you again soon! 🌟")
            break
        
        # Help
        elif 'help' in user_input or 'what can you do' in user_input:
            print("Bot: I can:")
            print("  • Greet you and chat")
            print("  • Tell you the current time and date")
            print("  • Do simple calculations (try: 'calculate 5+3')")
            print("  • Respond to various questions")
        
        # Default response
        else:
            responses = [
                "That's interesting! Tell me more.",
                "I'm still learning about that topic.",
                "Could you rephrase that? I'm a simple bot.",
                "I understand basic conversations. Try asking about time or saying hello!"
            ]
            import random
            print(f"Bot: {random.choice(responses)}")

# Main program to choose which chatbot to run
def main():
    print("Choose your chatbot:")
    print("1. Basic Chatbot (Simple)")
    print("2. Advanced Chatbot (More features)")
    
    choice = input("Enter 1 or 2: ").strip()
    
    if choice == "1":
        chatbot()
    elif choice == "2":
        advanced_chatbot()
    else:   
        print("Invalid choice. Starting basic chatbot...")
        chatbot()

# Run the chatbot
if _name_ == "_main_":
    main()
