import random

board = {}

def resetBoard():
       global board

       board = {1: " ", 2: " ", 3: " ",
                4: " ", 5: " ", 6: " ",
                7: " ", 8: " ", 9: " "}

resetBoard()
game = 9

def myBoard():
      print(board[1] + "|" + board[2] + "|" + board[3])
      print("-------------")
      print(board[4] + "|" + board[5] +"|"+ board[6])
      print("-------------")
      print(board[7] + "|" + board[8] +"|"+ board[9])
myBoard()      

game = 9


  
  


def mainGame(game):
 while range(0,len(board)):
  if board[1] =="X" and board[2]=="X" and board[3] == "X":
         print("victory")
         break
  elif board[4] =="X" and board[5] == "X" and board[6] =="X":
         print("victory")
         break      
  
  elif board[7] == "X" and board[8] == "X"and board[9] == "X":
         print("victory")
         break    
           
  elif board[1] and board[4] and board[7] == "X":
         print("victory")
         break
  
  elif board[2] and board[5] and board[8] == "X":
         print("victory")
         break
       
  elif board[3] and board[6] and board[9] == "X":
         print("victory")
         break  
     
  elif board[1] and board[5] and board[9] == "X":
         print("victory")
         break
  
  elif board[3] and board[5] and board[7] == "X":
         print("victory")
         break
  else:      
       key = int(input("ZADEJ POZICI"))
       value = "X"
       board[key] = value
       myBoard()


  def addO(value):
       #   for key in board:
       #          if value == " ":  // value != "X"
                 value = "O" 
                 key = random.randint(1,len(board))
                 while board[key] != " ":
                        key = random.randint(1,len(board))
                 board[key] = value
                 myBoard()
       #          else:
       #              addO()                      
        
  addO("O")  
  
        
      


  return mainGame(game-1)


   
mainGame(game)       
      
      

def endgame(a = input("One more?")):
       
       if a == "Yes":
              resetBoard()
              mainGame(game)
       elif a == "No":
          print("Goodbye")
          
          
endgame()       