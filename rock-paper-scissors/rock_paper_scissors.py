import random

# Introduction
print("Welcome to Rock, Paper, Scissors!")
print("First to 3 wins. Let's get it!")

# Keep track of scores
player_score = 0
computer_score = 0

#Available moves
moves = ["rock", "paper", "scissors"]

# Main game loop
while player_score < 3 and computer_score < 3:
    player_move = input("\nChoose rock, paper, or scissors: ").lower()

    if player_move not in moves:
        print("❌ Invalid choice. Try again.")
        continue

    computer_move = random.choice(moves)
    print(f"💻 Computer choose: {computer_move}")

    # Decide who wins
    if player_move == computer_move:
        print("🤝 It's a tie!")

    elif (
        (player_move == "rock" and computer_move == "scissors") or
        (player_move == "paper" and computer_move == "rock") or
        (player_move == "scissors" and computer_move == "paper")
    ):
        
        print("🎉 You win this round!")
        player_score += 1
    
    else:
        print("💔 You lose this round!")
        computer_score += 1
if player_score == 3:
    print("\n🎊 Congratulations, you won the game!")
else:
    print("\n😢 Sorry, you took an L. Better luck next time!")

# Ask to play again
play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again == "yes":

    # Reset scores
    player_score = 0
    computer_score = 0
    print("\n Starting a new game!")
    exec(open(__file__).read())
else:
    print("Thanks for playing! Goodbye!")

# Print current scores
print(f"🏆 Score - You: {player_score} | Computer: {computer_score}")

