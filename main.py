import random

def display_welcome_message():
    print("🎉 Welcome to the Super Fun Emoji Number Guessing Game! Let's have a blast! 🎉")
    print("🤔 I'm thinking of a number between 1 and 20. Can you guess it?")
    print("💡 Type 'exit' at any time to quit the game. Let's get started!")

def get_user_guess():
    while True:
        user_input = input("🤔 Your guess: ").strip().lower()
        if user_input == 'exit':
            return 'exit'
        if user_input.isdigit():
            return int(user_input)
        else:
            print("⚠️ Oops! Invalid input. Please enter a number.")

def evaluate_guess(secret_number, user_guess):
    if user_guess == secret_number:
        print(f"🎉 Woo-hoo! Congratulations! You guessed the number! You're a superstar! 🌟")
        return True
    elif user_guess < secret_number:
        print("📉 Oh no! Too low! But don't worry, give it another shot! 🚀")
    else:
        print("📈 Oopsie! Too high! But hey, you're getting closer! Keep going! 💪")
    return False

def play_game():
    secret_number = random.randint(1, 20)
    attempts = 0

    while True:
        user_guess = get_user_guess()
        if user_guess == 'exit':
            print("👋 Thanks for playing! See you next time!")
            return

        attempts += 1
        if evaluate_guess(secret_number, user_guess):
            break

if __name__ == "__main__":
    display_welcome_message()
    play_game()
