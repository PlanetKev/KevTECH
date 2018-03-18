import random
score = 0
games = int(input("How many games do you want to play: "))
games += 1
for i in range(1, games):
    print("Round " + str(i))
    choice = str(input("Choose 'Rock', 'Paper', or 'Scissors' "))
    list1 = ['Rock', 'Paper', 'Scissors']
    randomchoice = str(random.choice(list1))

    if choice == randomchoice:      # Tie
        print("My choice was " + randomchoice)
        print("We tied")

    # Rock Options
    elif choice == "Rock" and randomchoice == "Scissors":
        print("My choice was " + randomchoice)
        print("Rock beats scissors. You win!")
        score += 1
    elif choice == "Rock" and randomchoice == "Paper":
        print("My choice was " + randomchoice)
        print("Paper beats rock. You lose!")

    # Scissor Options
    elif choice == "Scissors" and randomchoice == "Paper":
        print("My choice was " + randomchoice)
        print("Scissors beats paper. You win!")
        score += 1
    elif choice == "Scissors" and randomchoice == "Rock":
        print("My choice was " + randomchoice)
        print("Rock beats scissors. You lose!")

    # Paper Options
    elif choice == "Paper" and randomchoice == "Scissors":
        print("My choice was " + randomchoice)
        print("Scissors beats paper. You lose!")
    elif choice == "Paper" and randomchoice == "Rock":
        print("My choice was " + randomchoice)
        print("Paper beats rock. You win!")
        score += 1
    print("")
games -= 1
print("Final Score: " + str(score) + " out of " + str(games) + " games")


