
import random
# Random module will be used for the computer moves. 

""" Bugs/Errors listed below """
# Bug: What happens when there is a draw? re scoreboard, re resetting tttBoard back to dashes -> Currently results in an indexError out of scope as it tries to get computers move
# Bug: When exiting the menu after a game played. It returns to main menu. Currently -> Temporary fix using exit() func. 
# 
#

class Scoreboard:
  """ Class used to store/view/update a scoreboard """
  def __init__(self): 
    self.scoreboard = {}

  def viewScore(self): # Haven't used this function yet. 
    for i,j in self.scoreboard.items(): 
      print (i.title() + ":", j)

  def isEmpty(self): 
    if self.scoreboard == {}: 
      return True
    return False 
  
  def updateScoreboard(self, winner: str):
    if winner.lower() in self.scoreboard:
      self.scoreboard[winner] += 1 
    else:
      self.scoreboard[winner] = 1
    return self.scoreboard
currentScore = Scoreboard()


def viewGrid(grid: list) -> list: # DONE
  """ function to print grid. Using recursion """ 
  
  # I got the idea of using recursion to print out each subgrid, from this video: 
  # https://www.youtube.com/watch?v=evOPQbevtaA

  def view(grid):
    if grid == []:
      return 
    else:
      print(grid[0], end=" ") 
      view(grid[1:])

  if grid == []:
    return
  else:
    view(grid[0])
    print()
    viewGrid(grid[1:])


def verifyGrid(grid: list, choice: str) -> bool: # DONE 
  """ Function to verify whether the game has been won by checking each row, column and diagonal given the move just made (x or an o) """ 


  def verifyRow(grid, choice): # Verifies each row
    for i in range(len(grid)): 
      if grid[i][0] == choice: 
        if grid[i][1] == choice:
          if grid[i][2] == choice: 
            return True
    return False

  if verifyRow(grid, choice) == True:
    return True


  def verifyColumn(grid, choice): # Verifies each col
    for i in range(len(grid)): 
      if grid[0][i] == choice: 
        if grid[1][i] == choice:
          if grid[2][i] == choice: 
            return True 
    return False 

  if verifyColumn(grid, choice) == True:
    return True
        

  def verify_Diag_RtoL(grid, choice): # Verifies diagonally from RtoL
    if grid[0][2] == choice: 
      if grid[1][1] == choice: 
        if grid[2][0] == choice: 
          return True
    return False 
  
  if verify_Diag_RtoL(grid, choice) == True:
    return True


  def verify_Diag_LtoR(grid, choice): # Verifies diagonally from LtoR
    if grid[0][0] == choice: 
      if grid[1][1] == choice: 
        if grid[2][2] == choice: 
          return True 
    return False
  
  if verify_Diag_LtoR(grid, choice) == True:
    return True
  

  return False 


def checkIfDraw(grid: list) -> bool: 
  """ Function to return true if the game has resulted in a draw """
  countMoves = 0 
  for i in range(len(grid)): 
    for j in grid[i]: 
      if j == "x" or j == "o":
        countMoves += 1 

  if verifyGrid == False and countMoves == 9: # meaning -> if the game has not been won (yet) AND all moves have been made (total 9)
    return True # then the game has been drawn


def changeGrid(coord: tuple, choice: str) -> list: # DONE
  """ function to change the global variable grid
      this will only accept valid coordinates from the user or computer, and return new tttBoard with that move """
  
  x,y = coord
  tttBoard[x][y] = choice
  return tttBoard 


def menu() -> int: # DONE
  """ function to display menu -> this will return the choice entered. this holds 2 functions, start game and view scoreboard """

  print ("\nMenu: \n"
        "+-+-+-+-+-+-+-+-+-+-+-+-+\n"
        "1) Player vs Comp\n"
        #"1.5) Multiplayer game out soon...\n"
        "2) Check scoreboard\n"
        "3) Exit game\n"
        )
  while True: 
    choice = input("What would you like to do? (Enter the corresponding digit): ")
    try:
      if int(choice) == 1: 
        return 1
      elif int(choice) == 2: 
        return 2 
      elif int(choice) == 3: 
        return 3 
      else: 
        print ("\nThat's not one of the options!\n")  
    except (ValueError):
      print ("Please enter a valid number. \n") 

  
def selection() -> str: # DONE
  """ Function returns "x" or "o" from user selection. Computer will be the opposite.
  Has no arguments """ 

  computer = ""
  print ("\nWould you like to be knoughts or crosses?")
  while True:
    choice = input("Enter \"o\" for knoughts, or \"x\" for crosses: ").lower().strip()
    if choice == "o":
      computer = "x" 
      print (f"\nYou have selected knoughts(o). The computer will be crosses (x). May the best player win!\n")
      return choice, computer 
    elif choice == "x":
      computer = "o"
      print (f"\nYou have selected crosses(x). The computer will be knoughts (o). May the best player win!\n")
      return choice, computer 
    else: 
      print ("\nIncorrect choice entered! Choose again.\n")


def getCoord() -> tuple: # DONE
  """ Function returns a tuple containing the coordinates of a grid user would like to enter """

  viewGrid(tttBoard)
  print()

  while True: 
    xVal = input("Please enter the row: ")
    yVal = input("Please enter the column: ")
    try:
      if (int(xVal) < 1) or (int(xVal) > 3) or (int(yVal) < 1) or (int(yVal) > 3): 
        print ("\nError! Please enter coordinates between 1 and 3 (inclusive): ")
      else: 
        return int(xVal)-1, int(yVal)-1
    except (ValueError): 
      print ("Please select a valid integer between 1 and 3.\n")


def verifyCoords(coords): # DONE
  """ function to return true or false if coordinates already occupy a knought or cross """

  x,y = coords
  if tttBoard[x][y] == "-":
    return True, coords 
  print ("Please enter a new set of coordinates. That space has already been occupied!" )
  return False 
  # returning false means that the coordinates given are already occupied with either an x or an o. 
  # if coordinates == true. run changeGrid()

def computerMove(computer: str) -> list: # DONE 
  """ function to fill in the computers moves """
  # this searches for all available moves and then selects a random coord. 
  
  lst = []
  for i in range(len(tttBoard)):
    for l, j in enumerate(tttBoard[i]): 
      if j == "-":
        tup = (i,l) # i,j is the outter grid , then the inner values
        lst.append(tup)
  
  a = random.choice(lst)
  tttBoard[a[0]][a[1]] = computer
  return tttBoard


def playAgain() -> list: 
  """ When user starts a new game, a freshboard will be returned to be used """
  tttBoard = []
  for _ in range(3):
    innerloop = [] 
    for _ in range(3): 
      innerloop.append("-")
    tttBoard.append(innerloop)
  return tttBoard


def main():
  """ Main function brings together the other functions required for the tttGame to work """
  global tttBoard # Global used here as it allows me to make changes to the board when a new game has restarted
  freshBoard = playAgain() # this function re runs each time main is called (each time user has started a new game)
  tttBoard = freshBoard 

  option = menu()

  if option == 1: 
    userChoice, computer = selection()

    if currentScore.isEmpty() == True: # this way it doesnt repeat each time the user starts a new game 
      print ("Choosing coordinates is simple 😀\n"
          "Enter a number between 1 and 3 for the row and another number for the column.\n")
      #viewGrid(tttBoard)
      print (freshBoard[0][0], freshBoard[0][1], freshBoard[0][2])
      print ("Above is each Row {->}")
      print ("Below is each Column {↓} ")
      print (freshBoard[0][0])
      print (freshBoard[1][0])
      print (freshBoard[2][0])
      print ("Choose wisely 😉\n")


    while True:


      # User moves, verifies move, updates grid, displays grid, and checks if that move was the winner
      coords = getCoord()
      while verifyCoords(coords) == False: 
        coords = getCoord()
      changeGrid(coords, userChoice)
      print ("\n...Updating TicTacToe Board...\n")
      viewGrid(tttBoard)
      
      # Below checks if the game has been won given the choice that has been made
      if (verifyGrid(tttBoard, userChoice)) == True:
        print (f"Game Over. You win!")
        currentScore.updateScoreboard("user")
        main() # this used to be menu()

      # elif checkIfDraw(tttBoard) == True: 
      #   print ("Game Over. The game has ended in a DRAW!")
      #   currentScore.updateScoreboard("computer")
      #   currentScore.updateScoreboard("user")
      #   main()

      else: 
        # Computer moves, displays grid, and checks if that move was the winner 
        computerMove(computer)
        print ("\n...Computer move below ...\n")
        if (verifyGrid(tttBoard, computer)) == True: 
          viewGrid(tttBoard)
          print (f"Game Over. Computer wins!")
          currentScore.updateScoreboard("computer")
          main()
      

  elif option == 2:

    if currentScore.isEmpty() == True: 
      print ("\nScoreboard unavailable.\n"
            "Start a game first!"
            )
      main()

    else: 
      print ("\n+-+-+-+-+-+-+-+-+-+\n"
             "Scoreboard : "
            )
      #currentScore.viewScore()
      for key,value in currentScore.scoreboard.items(): # Iterating through a Dicts keys and values 
        print (f"{key.title()} has {value} win(s)!") 
      print ("Keeping playing to gain more.")
      main()
      

  elif option == 3: 
    print ("-----------------\n"
          "+ Game exited +\n"
          "-----------------"
          )
    exit()
     

  else: 
    print ("Invalid option selected!")



if __name__ == "__main__":
  main()
