import random

# Function to get the user's choice
def get_user_choice():
    while True:
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_input in ['rock', 'paper', 'scissors']:
            return user_input
        else:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play a single round of the game
def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result

# Main game loop
def play_game():
    user_score = 0
    computer_score = 0

    while True:
        result = play_round()
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"Score: You - {user_score}, Computer - {computer_score}")
        
        # Ask if the player wants to continue
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
