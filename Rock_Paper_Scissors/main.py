from random import randint

def main():
    choices = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
    }
    is_play = input("Do you want to play? (y/n): ")
    attempts = 0
    win = 0
    lose = 0
    
    while is_play.lower() in ("y", "yes", "д", "да"):
        computer_choice = randint(1, 3)
        
        try:
           player_choice = int(input("\nEnter 1 for Rock, 2 for Paper, 3 for Scissors: "))
        except ValueError:
            print("\nInvalid input. Try again.")
            continue
        
        print(f"\nYour choice: {choices[player_choice]}")
        print(f"Computer's choice: {choices[computer_choice]}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
        elif player_choice == 1 and computer_choice == 3:
            print("\nYou win!")
            win += 1
        elif player_choice == 2 and computer_choice == 1:
            print("\nYou win!")
            win += 1
        elif player_choice == 3 and computer_choice == 2:
            print("\nYou win!")
            win += 1
        else:
            print("\nYou lose!")
            lose += 1
        
        attempts += 1
        is_play = input("Do you want to play again? (y/n): ")
    
    print(f"\nYou played {attempts} times. You won {win} times and lost {lose} times.")
    print("Goodbye!")
    
if __name__ == "__main__":
    main()
    
    
    