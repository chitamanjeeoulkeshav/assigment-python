name1 = input("Name of the first player: \n")
name2 = input("Name of the second player: \n")


def check(player1, player2):
    if player1 != "Rock" and player1 != "Paper" and player1 != "Scissors":
        print("You have not entered rock, paper or scissors. Try again.\n")

    elif player2 != "Rock" and player2 != "Paper" and player2 != "Scissors":
        print("You have not entered rock, paper or scissors. Try again.\n")


def game(player1, player2):
    if player1 == player2:
        print("It\'s a draw! Try again.\n")

    elif player1 == "Rock":
        if player2 == "Scissors":
            print(name1 + " congratulations!\n")
        else:
            print(name2 + " congratulations!\n")

    elif player1 == "Paper":
        if player2 == "Scissors":
            print(name2 + " congratulations!\n")
        else:
            print(name1 + " congratulations!\n")

    elif player1 == "Scissors":
        if player2 == "Rock":
            print(name2 + " congratulations!\n")
        else:
            print(name1 + " congratulations!\n")


while True:
    player1 = str(input("Rock, paper or scissors?\n"))
    player2 = str(input("Rock, paper or scissors?\n"))

    check(player1, player2)
    game(player1, player2)

    answer = str(input("Do you want to start a new game? Enter \"Yes\" or \"No\".\n\n"))

    if answer == "No":
        break