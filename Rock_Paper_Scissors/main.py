from random import randint

def main():
    choices = {
        1: "Rock",
        2: "Paper",
        3: "Scissors"
    }
    isPlay = input("Do you want to play? (y/n): ")
    attempts = 0
    win = 0
    lose = 0
    
    while isPlay == "y" or isPlay == "Y" or isPlay == "yes" or isPlay == "Yes" or isPlay == "YES" or isPlay == "д" or isPlay == "Д" or isPlay == "да" or isPlay == "Да":
        player_choice = int(input("\nEnter 1 for Rock, 2 for Paper, 3 for Scissors: "))
        computer_choice = randint(1, 3)
        
        if player_choice < 1 or player_choice > 3:
            print("\nInvalid input!")
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
        isPlay = input("Do you want to play again? (y/n): ")
    
    print(f"\nYou played {attempts} times. You won {win} times and lost {lose} times.")
    print("Goodbye!")
    
main()
    
    
    