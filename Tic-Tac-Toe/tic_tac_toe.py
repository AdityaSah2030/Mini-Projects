import time 
import random
import os


def game_instructions():
    print("It is similar to the basic tic-tac-toe game which we scribble on paper.\n")
    print("The only difference lies here is that you have to interact with the system with help of 1 to 9 number keys.\n ")

def board():
    pass

def def_board():
    board = range(1,10)
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
    print("-----------------")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
    print("-----------------")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")

def print_board(posn, user):
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if posn == 1:
        if user == 1:
            board[posn-1] = "X"
        else:
            board[posn-1] = "O"
        print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
        print("-----------------")
        print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
        print("-----------------")
        print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")

    elif posn == 2:
        if user == 1:
            board[posn-1] = "X"
        else:
            board[posn-1] = "O"
        print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
        print("-----------------")
        print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
        print("-----------------")
        print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")

    elif posn == 3:
        if user == 1:
            board[posn-1] = "X"
        else:
            board[posn-1] = "O"
        print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
        print("-----------------")
        print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
        print("-----------------")
        print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")

    elif posn == 4:
        if user == 1:
            board[posn-1] = "X"
        else:
            board[posn-1] = "O"
        print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
        print("-----------------")
        print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
        print("-----------------")
        print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")

    elif posn == 5:
        if user == 1:
            board[posn-1] = "X"
        else:
            board[posn-1] = "O"
        print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
        print("-----------------")
        print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
        print("-----------------")
        print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")

    elif posn == 6:
        if user == 1:
            board[posn-1] = "X"
        else:
            board[posn-1] = "O"
        print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
        print("-----------------")
        print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
        print("-----------------")
        print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")    

    elif posn == 7:
        if user == 1:
            board[posn-1] = "X"
        else:
            board[posn-1] = "O"
        print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
        print("-----------------")
        print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
        print("-----------------")
        print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")

    elif posn == 8:
        if user == 1:
            board[posn-1] = "X"
        else:
            board[posn-1] = "O"
        print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
        print("-----------------")
        print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
        print("-----------------")
        print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")

    elif posn == 9:
        if board[posn] == "X" or board[posn] == "O":
            if user == 1:
                board[posn-1] = "X"
            else:
                board[posn-1] = "O"
        else:
            print(Position already occupied. Please choose another position.) 
        print(f"  {board[0]}  |  {board[1]}  |  {board[2]}  ")
        print("-----------------")
        print(f"  {board[3]}  |  {board[4]}  |  {board[5]}  ")
        print("-----------------")
        print(f"  {board[6]}  |  {board[7]}  |  {board[8]}  ")

    else:
        print("Invalid position. Please enter a number between 1 and 9.")


    print(f"  {board[0]}  |  {board[1]}  |

def with_friend():
    for i in range(1,9,1):
        place = input(f"{name}, enter the position where you want to place your turn (1 to 9): ")
        def print_board(place)

def with_computer():
    pass

def main():
    while True:
        game_instructions()
        print_board()

        global name 
        name = input("\nEnter your name: ")

        print(f"\nWelcome {name} to Tic Tac Toe game.\n")
        print("Choose how you want to play the game: ")
        print("1. Play with Computer")
        print("2. Play with Friend")
        choice = int(input("Enter your choice (1/2): "))

        if choice == 1:
            print("You will play as X and Computer will play as O.\n")
            with_computer()

        elif choice == 2:
            global name2 
            name2 = input("Enter the name of your friend: ")
            print(f"You will play as X and {name2} will play as O.\n")
            with_friend()

        else:
            print("Invalid choice. Please choose 1 or 2.\n")


if __name__ == "__main__":
    main()