#Make the tictac board
board = ["  " for i in range(9)]

def print_board():
    row1 = "|{}|{}|{}|".format(board[0],board[1],board[2])
    row2 = "|{}|{}|{}|".format(board[3],board[4],board[5])
    row3 = "|{}|{}|{}|".format(board[6],board[7],board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()



#take user input and mark the cell
def mark_cell(icon):
    if icon == "X":
        number =1
    elif icon == "O":
        number  =2
    #print("Enter {} player {}".format(icon, number))
    choice = int(input("Enter the cell number 1-9 to mark {} Player-{}: ".format(icon, number)).strip())
    if(choice):
        if board[choice-1]=="  ":
            board[choice-1] =icon
        else:
            print()
            print("The cell is already marked")

def is_win(icon):
    if(board[0]==icon and board[1]==icon and board[2]==icon) or \
      (board[6]==icon and board[7]==icon and board[8]==icon) or \
      (board[0]==icon and board[3]==icon and board[6]==icon) or \
      (board[1]==icon and board[4]==icon and board[7]==icon) or \
      (board[2]==icon and board[5]==icon and board[8]==icon) or \
      (board[0]==icon and board[4]==icon and board[8]==icon) or \
      (board[3]==icon and board[4]==icon and board[5]==icon) or \
      (board[2]==icon and board[4]==icon and board[6]==icon):
          return True
    else:
        return False

def is_no_Win():
    if "  " not in board:
        return True
    else:
        return False
    
while True:
    
    mark_cell("X")
    print_board()
    if is_win("X"):
        print("Player 1 wins. Congrats")
        break
    elif is_no_Win():
        print("Draw !!")
        break
    mark_cell("O")
    print_board()
    if is_win("O"):
        print_board()
        print("Player 2 wins. Congrats")
        break
    elif is_no_Win():
        print("Draw !!")
        break
    


