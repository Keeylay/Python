import random

while True:
    manygames = int(input("Enter a number for how many games do you want to play "))
    for i in range(manygames):
        if (manygames > 0):
            manygames = manygames - 1

            action = input("Enter one of the following: Rock, Paper, Scissors:")
            possibilities = ["Rock", "Paper", "Scissors"]
            computerchoice = random.choice(possibilities)

            #win conditions
            if action == computerchoice:
                print("Its a tie!")
            elif action == "Rock":
                if computerchoice == "Scissors":
                    print("Rock smashes Scissors! You win!")
                else:
                    print("Rock cant win against Paper! You Lose!")
            elif action == "Paper":
                if computerchoice == "Scissors":
                    print("Scissors slices your Paper! You Lose!")
                else: 
                    print("Rock cant win against Paper! You Win!")
            elif action == "Scissors":
                if computerchoice == "Paper":
                    print("Scissors slices the Paper! You Win!")
                else:
                    print("Rock smashes Scissors! You Lose!")
        
            print(f"You choose {action} and the computer choose {computerchoice}.")
            
            if (manygames != 0):
                continue
            else:
                quit()
