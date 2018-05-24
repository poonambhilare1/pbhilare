from IPython.display import clear_output
import sys
from __future__ import print_function 


if __name__ == "__main__":
    # Support Python 2 and 3 input
    # Default to Python 3's input()
    get_input = input
    
if sys.version_info[:2] <= (2, 7):      
    get_input = raw_input
    
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
win=0

mark='x'
player1 = raw_input("Enter the player1 name ") 
player2 = raw_input("Enter the player2 name ") 
player = 1
def DrawBoard():    
    print(" %c | %c | %c " % (board[0],board[1],board[2]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[3],board[4],board[5]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[6],board[7],board[8]))    
    print("   |   |   ") 

def checkWin():
    global win
   
    
    if(board[0] == board[1] and board[1] == board[2] and board[0] != ' '):  
        win=1
    if(board[0] == board[4] and board[4] == board[8] and board[0] !=' '):
        win=1;
    if(board[0]==board[3] and board[3]==board[6] and board[0]!=' '):
        
        win=1
    if(board[1]==board[4] and board[4]==board[7] and board[1]!=' '):
        
        win=1
    if(board[2]==board[5] and board[5]==board[8] and board[2]!=' '):
       
        win=1
    if(board[2]==board[4] and board[4]==board[7] and board[2]!=' '):
       
        win=1
    if(board[3]==board[4] and board[4]==board[5] and board[3]!=' '):
        win=1    
    if(board[6]==board[7] and board[7]==board[8] and board[6]!=' '):
        win=1;
    elif(board[0]!=' ' and board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' '):
        win=2;    
        
def checkPosition(x):
    if(board[x]==' '):
        return True
    else:
        return False
def inputPosition():
    choice=''
    while choice not in ['0','1','2','3','4','5','6','7','8']:
         choice = raw_input("Enter the position between [0-8] where you want to mark : ")
    return int(choice)
        
    
while(True):
    clear_output()
    DrawBoard()    
    if(win == 0):   
        if(player % 2 != 0):    
            print(player1+" chance")    
            mark = 'X'
        else:
            print(player2+" chance")    
            mark = 'O'  
        choice=inputPosition()
        if(checkPosition(choice)):
            board[choice] = mark 
            player+=1  
            checkWin()
        else:
            print('\033[0;37;41m wrong choice please enter again  \033[0m ')
            
    elif(win != 0):              
        break
        
if(win == 1):
    
    if(player-1 % 2 != 0):
        print("winner is %s"%(player1))
    else:
        print("winner is %s"%(player2))
    
if(win==2):
    print("game is draw") 

    
    

    