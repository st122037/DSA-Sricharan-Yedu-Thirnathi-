def winning_conditions(l):
     winner = 'null' 
     for i in range(len(l)):
         if   l[i][0] == l[i][1] and l[i][1] == l[i][2] and l[i][0] != '_':
             winner = l[i][0]

     for i in range(len(l)):
         if   l[0][i] == l[1][i] and l[1][i] == l[2][i] and l[0][i] != '_':
             winner = l[0][i]

     if      l[0][0] == l[1][1]  and l[1][1] == l[2][2] and l[0][0] != '_':
         winner = l[0][0]

     if    l[0][2] == l[1][1]  and l[1][1] == l[2][0] and l[0][2] != '_':
         winner = l[0][2]

     if len(possible_moves(l))==0 and winner == 'null':
         winner = 'tie'

     if  winner == None:
         return(None)
     else:
         return(winner)

def print_grid(l):
     for i in range(len(l)):
         print("|".join(l[i]))

def possible_moves(l):
     blank_moves = []
     for i in range(len(l)):
         for j in range(len(l[i])):
             if l[i][j] == '_':
                 blank_moves.append([i,j])
     return(blank_moves)

scores = {
     'X'    : 1,
     'o'    : -1,
     'tie'  : 0
 }

def minmax(l, depth, isMaximizing):
     result = winning_conditions(l)

     if result != "null":
         return(scores[result])

     if isMaximizing:
         bestscore = -100
         blank_spaces = possible_moves(l)
         for [x,y] in blank_spaces:
             l[x][y] = 'X'
             score = minmax(l, depth+1, False)
             l[x][y] = '_'
             bestscore = max(score, bestscore)

         return(bestscore)

     else:
         bestscore = 100
         blank_spaces = possible_moves(l)
         for [x,y] in blank_spaces:
             l[x][y] = 'o'
             score = minmax(l, depth+1, True)
             l[x][y] = '_'
             bestscore = min(score,bestscore)

         return(bestscore)

def computer_move(l):
     blank_moves = possible_moves(l)
     k = []

     if len(blank_moves)>0:
         bestscore = 100
         for [x,y] in blank_moves:
             l[x][y]= 'o'
             score = minmax(l, 0, True)
             l[x][y]= '_'
             if score < bestscore:
                 bestscore = score
                 k = [x, y]

         l[k[0]][k[1]] = 'o'
         print("computer played its move!")
     else:
         print(winning_conditions(l))


def main():
     grid = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
     print_grid(grid)
     print("="*30)
     print("TIC TAC TOE")
     print("="*30)
     while len(possible_moves(grid))>0:
         x, y = input("Enter your choice:").split(" ")
         x, y = int(x), int(y)
      
         blank_space = possible_moves(grid)
         
         for [z,v] in blank_space:
           if grid[z][v] == grid[x][y]:
             grid[x][y] = 'X'
         print_grid(grid)
         computer_move(grid)
         print_grid(grid)
         print("="*25)
         if (winning_conditions(grid)) == 'o':
             print("="*25)
             print("COMPUTER WON!!!!!!")
             print("="*25)
             break
         elif winning_conditions(grid) == 'X':
             print("="*25)
             print("PLAYER WON!!!!!!")
             print("="*25)
             break
         elif winning_conditions(grid) == 'tie':
             print("="*25)
             print("IT WAS A TIE, SORRY YOU CAN'T BEAT ME")
             print("="*25)
             break

main()