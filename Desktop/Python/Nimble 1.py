# Python Project 1, game 


import random   #imports the random module from library
                #Used for randomly generating pawns


def MainBoard(n, pawn):
    while True:
        Empty_cells = 0                         # Set to count the amount of empty cells ( to be used in play condition )
        Display_Board = []                      # Empty list to be displayed as Board

        for items in range(n):
            pawn = random.randint(0, pawn)      # Random number of pawns from 0 to "p" value in each square
            Display_Board.append(pawn)
            print(pawn)                         # Used to verify if pawns are being appended ( to be removed in final work )

        for cells in Display_Board:
            if cells == 0:
                Empty_cells += 1                # Increments count for empty cells 

        print(f"Empty Cells  = {Empty_cells}")     #Displays U
        if (n - 1) > Empty_cells:
            return Display_Board

MainBoard(5, 5)   #dummy values for testing 