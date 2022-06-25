import random

while True:
    pilihan = ["kertas","batu","gunting"]

    computer = random.choice(pilihan)
    player = None

    while player not in pilihan:
        player = input("\nkertas,batu,gunting? : ")

    if player == computer:
        print("\ncomputer : "+ str(computer))
        print("player : "+ str(player))
        print("draw!")
    elif player == "batu":
        if computer == "kertas":
            print("\ncomputer : " + str(computer))
            print("player : " + str(player))
            print("kamu kalah:(")
        if computer == "gunting":
            print("\ncomputer : " + str(computer))
            print("player : " + str(player))
            print("kamu menang!")
    elif player == "gunting":
        if computer == "batu":
            print("\ncomputer : " + str(computer))
            print("player : " + str(player))
            print("kamu kalah:(")
        if computer == "kertas":
            print("\ncomputer : " + str(computer))
            print("player : " + str(player))
            print("kamu menang!")
    elif player == "kertas":
        if computer == "gunting":
            print("\ncomputer : " + str(computer))
            print("player : " + str(player))
            print("kamu kalah:(")
        if computer == "batu":
            print("\ncomputer : " + str(computer))
            print("player : " + str(player))
            print("kamu menang!")

    main_lagi = input("\nLanjutkan permainan? (yes/no) : ").lower()

    if main_lagi != "yes":
        break

print("Bye:)")