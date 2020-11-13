#Tic-Tac-Toe Computer vs Computer Program
#Here the two players use '1' and '9' as their pawns for Tic tca Toe, hence a numpy array is used

import numpy as np 
import random 
from time import sleep 
  
# Creation of an empty board 
def create_board(): 
    return(np.array([[0, 0, 0], 
                     [0, 0, 0], 
                     [0, 0, 0]])) 
  
# Check for empty places on board 
def check_for_space(board): 
    l = [] 
      
    for i in range(len(board)): 
        for j in range(len(board)): 
              
            if board[i][j] == 0: 
                l.append((i, j)) 
    return(l) 
  
# Select a random place for the player 
def random_place(board, player): 
    selection = check_for_space(board) 
    current = random.choice(selection) 
    board[current] = player 
    return(board) 
  
# Checks whether the player has three  
# of their marks in a horizontal row to make them win
def row_checking(board, player): 
    for i in range(len(board)): 
        win = True
          
        for j in range(len(board)): 
            if board[i, j] != player: 
                win = False
                continue
                  
        if win == True: 
            return(win) 
    return(win) 
  
# Checks whether the player has three 
# of their marks in a vertical row to make them win
def col_checking(board, player): 
    for i in range(len(board)): 
        win = True
          
        for j in range(len(board)): 
            if board[j][i] != player: 
                win = False
                continue
                  
        if win == True: 
            return(win) 
    return(win) 
  
# Checks whether the player has three 
# of their marks in a diagonal row to make them win
def diag_checking(board, player): 
    win = True
    j = 0
    for i in range(len(board)): 
        if board[i, i] != player: 
            win = False
    if win: 
        return win 
    win = True
    if win: 
        for i in range(len(board)): 
            j = len(board) - 1 - i 
            if board[i, j] != player: 
                win = False
    return win 
  
# a winner or a tie - Decision making time
 
def what_is_the_final_result(board): 
    winner = 0
      
    for player in [1, 2]: 
        if (row_checking(board, player) or
            col_checking(board,player) or 
            diag_checking(board,player)): 
                 
            winner = player 
              
    if np.all(board != 0) and winner == 0: 
        winner = -1
    return winner 
  
# Main function to start the game 
def play_now(): 
    board, winner, counter = create_board(), 0, 1
    print(board) 
    sleep(2) 
      
    while winner == 0: 
        for player in [1,9]: 
            board = random_place(board,player) 
            print("Board after " + str(counter) + " move") 
            print(board) 
            sleep(2) 
            counter += 1
            winner = what_is_the_final_result(board) 
            if winner != 0: 
                break
    return(winner) 
  
  
print("Winner is: " + str(play_now())) 