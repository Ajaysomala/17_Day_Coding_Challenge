### ---- Day 7 Challenge ---- ###

# Simple Chat Bot Using Using Day Practises....../


import time

def chat_bot(command, **kwargs):
    username = kwargs.get("name", "User")  # Default name is "User"
    mood = kwargs.get("mood", "Okay")      # Optional mood

    if command.lower() == "hello":
        print(f"Hi {username}! How are you feeling today?")
    elif command.lower() == "time":
        current_time = time.strftime("%I:%M %p")
        print(f"{username}, current time is: {current_time}")
    elif command.lower() == "mood":
        print(f"You're feeling {mood} today. Hope your day gets better, {username}! ☀️")
    elif command.lower() == "help":
        print("Available commands: hello, time, mood, help, exit")
    elif command.lower() == "exit":
        print("Goodbye! Have a great day!")
    else:
        print("Sorry, I don't understand that. Type 'help' to see what I can do.")

# 💬 CLI simulation
while True:
    cmd = input("\nYou: ")
    if cmd.lower() == "exit":
        chat_bot("exit", name="Beru")
        break
    elif cmd.lower() == "mood":
        user_mood = input("What's your mood today? 😊: ")
        chat_bot("mood", name="Beru", mood=user_mood)
    else:
        chat_bot(cmd, name="Beru")
