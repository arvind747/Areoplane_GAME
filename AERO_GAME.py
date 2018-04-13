import sched, time
import os
import random
s = sched.scheduler(time.time, time.sleep)

string = ''
Aeroplane = ['-','|',]
display = []
game_Over = False

#Initialize Display
def Display_Init():
    global display
    display = []
    for i in range(20):
       display.append([])
       for j in range(24):
          display[i].append('.')

#Dispay CPU plane
def Form_Display(row,column_1,column_2):
    global display
    display[row][2+column_1] = '_'
    display[row+1][2+column_1] = '|'
    display[row+1][3+column_1] = '|'
    display[row+1][1+column_1] = '_'
    display[row+1][4+column_1] = '_'
    display[row+2][1+column_1] = '|'
    display[row+2][4+column_1] = '|'
    display[row+2][2+column_1] = '_'
    display[row+2][3+column_1] = '_'
    display[row+3][2+column_1] = '|'
    display[row+3][3+column_1] = '|'
    display[row+3][1+column_1] = '_'
    display[row+3][4+column_1] = '_'

    display[row][2 + column_2] = '_'
    display[row+1][2 + column_2] = '|'
    display[row+1][3+ column_2] = '|'
    display[row+1][1+ column_2] = '_'
    display[row+1][4+ column_2] = '_'
    display[row+2][1+ column_2] = '|'
    display[row+2][4+ column_2] = '|'
    display[row+2][2+ column_2] = '_'
    display[row+2][3+ column_2] = '_'
    display[row+3][2+ column_2] = '|'
    display[row+3][3+ column_2] = '|'
    display[row+3][1+ column_2] = '_'
    display[row+3][4+ column_2] = '_'

#Get USER input(user plane position) on console
def get_input_from_usr():
    return int(raw_input("Enter index"))

#Clear Display
def clear_display(start,end):
    global display
    for i in range(start, end):
       for j in range(24):
          display[i][j] = '.'

#Check for GAME OVER          
def check_out(num):
    global display
    global game_Over
    if (display[15][2 + num] != '.'  or  
       display[15+1][2 + num] != '.' or 
       display[15+1][3+ num] != '.'  or 
       display[15+1][1+ num] != '.'  or 
       display[15+1][4+ num] != '.'  or 
       display[15+2][1+ num] != '.'  or 
       display[15+2][4+ num] != '.'  or 
       display[15+2][2+ num] != '.'  or 
       display[15+2][3+ num] != '.'  or 
       display[15+3][2+ num] != '.'  or 
       display[15+3][3+ num] != '.'  or 
       display[15+3][1+ num] != '.'  or 
       display[15+3][4+ num] != '.' ):
       game_Over = True
       
       display[2][0] = '-'
       display[2][1] = '-'
       display[2][2] = '-'
       display[2][3] = '-'
       display[2][4] = '-'
       display[3][0] = '|'
       display[4][0] = '|'
       display[5][0] = '-'
       display[5][1] = '-'
       display[5][2] = '-'
       display[5][3] = '-'
       display[5][4] = '-'
       display[5][5] = '|'
       display[4][5] = '|'
       display[3][5] = '-'
       display[3][4] = '-'


       display[2][8] = '-'
       display[2][9] = '-'
       display[2][10] = '-'
       display[2][11] = '-'
       display[3][8] = '|'
       display[4][8] = '|'
       display[4][9] = '-'
       display[4][10] = '-'
       display[4][11] = '-'    
       display[5][8] = '|'
       display[2][4] = '-'
       display[3][0] = '|'
       display[4][0] = '|'
       display[5][0] = '-'
       display[5][1] = '-'
       display[5][2] = '-'
       display[5][3] = '-'
       display[5][4] = '-'
       display[5][5] = '|'
       display[4][5] = '|'
       display[3][5] = '-'
       display[3][4] = '-'
       
#M
       display[2][16] = '|'
       display[3][16] = '|'
       display[4][16] = '|'
       display[5][16] = '|'
       display[2][17] =  '-'
       display[2][18] =  '/'
       display[2][13] = '-'
       display[3][8] = '|'
       display[4][8] = '|'
       display[4][9] = '-'
       display[4][10] = '-'
       display[4][11] = '-'
       display[4][12] = '-'    
       display[5][8] = '|'
       display[3][13] = '|'
       display[4][13] = '|'
       display[5][13] = '|'
       display[2][4] = '-'
       display[3][0] = '|'
       display[4][0] = '|'
       display[5][0] = '-'
       display[5][1] = '-'
       display[5][2] = '-'
       display[5][3] = '-'
       display[5][4] = '-'
       display[5][5] = '|'
       display[4][5] = '|'
       display[3][5] = '-'
       display[3][4] = '-'

#E       
       
       display[15][2 + num] = '|'
       display[15+1][3+ num] = '|'
       display[15+1][1+ num] = '_'
       display[15+1][4+ num] = '_'
       display[15+2][1+ num] = '|'
       display[15+2][4+ num] = '|'
       display[15+2][2+ num] = '_'
       display[15+2][3+ num] = '_'
       display[15+3][2+ num] = '|'
       display[15+3][3+ num] = '|'
       display[15+3][1+ num] = '_'
       display[15+3][4+ num] = '_'

       
#Form user plane on console                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
def form_user_input(num):
    global display
    clear_display(15,20)      
          
    display[15][2 + num] = '_'
    display[15+1][2 + num] = '|'
    display[15+1][3+ num] = '|'
    display[15+1][1+ num] = '_'
    display[15+1][4+ num] = '_'
    display[15+2][1+ num] = '|'
    display[15+2][4+ num] = '|'
    display[15+2][2+ num] = '_'
    display[15+2][3+ num] = '_'
    display[15+3][2+ num] = '|'
    display[15+3][3+ num] = '|'
    display[15+3][1+ num] = '_'
    display[15+3][4+ num] = '_'

#display GAME on Console    
def Display_plane():
    global display
    sring = ' '
    for i in range(20):
       string = ''
       for j in range(24):
          string += display[i][j]
       print string

#shift last row diasplay
def Shift_Display(loopCount):
    global display
    rev = 19
    for iloop in range(5,20):
        for jloop in range(24):
            display[rev][jloop] = display[rev - 5][jloop]
        rev = rev - 1

#Initialize variable              
current_Pos = 0       
Display_Init()
row,col = 20,2
row_display = [[0 for x in range(col)] for y in range(row)]

#Generate Random Areoplane display 
for rand_display_gen in range(0,20):
    row_display[rand_display_gen][0] = random.randint(0,7)
    row_display[rand_display_gen][1] = random.randint(12,19)

#Play GAME   
for k in range(4):
    i = 0
    if k == 0:
       for i in range(5):
           clear_display(0, i*5)

           i_count = i
           for i_index in range(0, i):
               if (i_count > 0):
                   Form_Display((i_count - 1)*5,row_display[i_index + k *5][0], row_display[i_index + k * 5][1])
                   i_count = i_count - 1

           ip = get_input_from_usr()
           privious_Pos = current_Pos
           current_Pos = ip
           if(current_Pos != privious_Pos):
              check_out(ip*5)

           form_user_input(ip*5)
           Display_plane()
           s.delayfunc(2)

           if bool(game_Over) == True:
              break
           else:
              continue
    else:
        ip = get_input_from_usr()
        privious_Pos = current_Pos
        current_Pos = ip
        if(current_Pos != privious_Pos):
           check_out(ip*5)
              
        form_user_input(ip*5)
        Display_plane()
        s.delayfunc(2)
        Shift_Display(k)
        clear_display(0, 5)
        Form_Display(0,row_display[k+5][0], row_display[k+5][1])                

    if bool(game_Over) == True:
       break
    else:
       continue
