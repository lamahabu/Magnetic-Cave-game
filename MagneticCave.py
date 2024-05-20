#Sami Moqbel : 1200751
#Lama Abdelmohsen : 1201138
#AI Magnetic Cave Game
#“We certify that this submission is the original work of members of the group and meets
#the Faculty's Expectations of Originality
#6/20/2023

import copy

COLUMNS=10
ROWS=10
BLACK="\u25A2"
WHITE="\u25A0"
BOARD = [["" for _ in range(COLUMNS)] for _ in range(ROWS)]
PLAYER=BLACK
twoWConnected=False
threeWConnected=False
fourWConnected=False
twoBConnected=False
threeBConnected=False
fourBConnected=False


def playAMove():
    coordinates=[0,0]
    while True:

        if PLAYER== BLACK:
            player="PLAYER 1"
        else:
            player="PLAYER 2"

        testInput=input(f"[{player}] Please enter position: ")
        testInput=testInput.lower()
        #print(testInput)
        coordinates[0]=ROWS-int(testInput[0])-1
        if (int(testInput[0]) < 1 or int(testInput[0]) > 8):
            print("WRONG INPUT !!")
        else:
            if testInput[1] == "a":
                #print("A tempColumn")
                coordinates[1]=1
                #BOARD[ROWS-int(testInput[0])-1][1]=WHITE
                break
            elif testInput[1] == "b":
                #print("B tempColumn")
                coordinates[1] = 2
                break
            elif testInput[1] == "c":
                #print("c tempColumn")
                coordinates[1] = 3
                break
            elif testInput[1] == "d":
                #print("d tempColumn")
                coordinates[1] = 4
                break
            elif testInput[1] == "e":
                #print("e tempColumn")
                coordinates[1] = 5
                break
            elif testInput[1] == "f":
                #print("f tempColumn")
                coordinates[1] = 6
                break
            elif testInput[1] == "g":
                #print("g tempColumn")
                coordinates[1] = 7
                break
            elif testInput[1] == "h":
                #print("h tempColumn")
                coordinates[1] = 8
                break
            else:
                print("WRONG INPUT!!")
    #print(f"RETURN IS {coordinates}")
    return coordinates

def printMenu():
    print("1) Player vs Player")
    print("2) Player vs Bot (Player starts first)")
    print("3) Player vs Bot (Bot starts first)")
    print("4) EXIT ! ")


def printBoard(board):

    #Upper BORDER OF ABCDEFGH
    print(f"\t\t{board[0][1]}\t\t{board[0][2]}\t\t{board[0][3]}\t\t{board[0][4]}\t\t{board[0][5]}\t\t{board[0][6]}\t\t{board[0][7]}\t\t{board[0][8]}\t\t{board[0][9]}\t")
    print("\t-----------------------------------------------------------------")

    #ITERATE THROUGH 1 to 8 because first and last rows are for BORDER
    for index, row in enumerate(board[1:9], start=1):
        print(f"{row[0]}\t|\t{row[1]}\t|\t{row[2]}\t|\t{row[3]}\t|\t{row[4]}\t|\t{row[5]}\t|\t{row[6]}\t|\t{row[7]}\t|\t{row[8]}\t|\t{row[9]}\t")
        print("\t-----------------------------------------------------------------")

    # Lower BORDER OF ABCDEFGH
    print(f"\t\t{board[9][1]}\t\t{board[9][2]}\t\t{board[9][3]}\t\t{board[9][4]}\t\t{board[9][5]}\t\t{board[9][6]}\t\t{board[9][7]}\t\t{board[9][8]}\t\t{board[9][9]}\t")



def changeTurn():
    global PLAYER

    if (PLAYER == BLACK ):
        PLAYER = WHITE
    else:
        PLAYER = BLACK


def emptySpots():
    moves=[]
    for row in range(1,ROWS):
          for col in range(1,COLUMNS):
              if BOARD[row][col] =="":
                move = (row, col)  # Create a tuple with the row and column
                moves.append(move)  # Store the tuple in the moves list
    return  moves

def availableSpots():
    availableMoves=[]
    starterColumn=1
    latestColumn=8

    for row in range(1,ROWS-1):
        starterColumn = 1
        if(BOARD[row][starterColumn]==""):
            availableMoves.append((row,starterColumn))
        else:
            while(BOARD[row][starterColumn] !="" and starterColumn+1 < 9):
                starterColumn=starterColumn+1
                #print(f"STARTER {starterColumn}")
            if (BOARD[row][starterColumn] == WHITE or BOARD[row][starterColumn]== BLACK):
                pass
            else:
                availableMoves.append((row,starterColumn))


    for row in range(1,ROWS-1):
        latestColumn = 8
        if(BOARD[row][latestColumn]==""):
            availableMoves.append((row,latestColumn))
        else:

            while(BOARD[row][latestColumn] !="" and latestColumn-1 > 0):
                latestColumn=latestColumn-1
                #print(f"LATEST {latestColumn}")
            if (BOARD[row][latestColumn] == WHITE or BOARD[row][latestColumn] == BLACK):
                pass
            else:
                availableMoves.append((row,latestColumn))

    return set(availableMoves)



def winnerIsBlack():
    # Check horizontal winning
    for row in range(1,ROWS-1):
        for col in range(1,COLUMNS - 5):
            if (BOARD[row][col] ==BLACK and
                BOARD[row][col + 1] == BLACK and
                BOARD[row][col + 2] == BLACK and
                BOARD[row][col + 3] == BLACK and
                BOARD[row][col + 4] == BLACK):
                    return True
    for row in range(1,ROWS - 5):
        for col in range(1,COLUMNS-1):
            if (BOARD[row][col] == BLACK and
                BOARD[row + 1][col] ==BLACK and
                BOARD[row + 2][col] ==BLACK and
                BOARD[row + 3][col] ==BLACK and
                BOARD[row + 4][col] ==BLACK):
                    return True

    for row in range(1,ROWS - 5):#needs update
        for col in range(1,COLUMNS - 5): #needs update
            if (BOARD[row][col] == BLACK and
                BOARD[row + 1][col + 1] == BLACK and
                BOARD[row + 2][col + 2] == BLACK and
                BOARD[row + 3][col + 3] == BLACK and
                BOARD[row + 4][col + 4] == BLACK):
                    return True

    for row in range(5, ROWS):
        for col in range(1,COLUMNS - 5):
            if (BOARD[row][col] == BLACK and
                BOARD[row -1 ][col + 1] == BLACK and
                BOARD[row -2][col + 2] == BLACK and
                BOARD[row -3][col + 3] == BLACK and
                BOARD[row -4][col + 4] == BLACK):
                    return True

    return False


def winnerIsWhite():
    # Check horizontal winning
    for row in range(1,ROWS-1):
        for col in range(1,COLUMNS - 5):
            if (BOARD[row][col] ==WHITE and
                BOARD[row][col + 1] == WHITE and
                BOARD[row][col + 2] == WHITE and
                BOARD[row][col + 3] == WHITE and
                BOARD[row][col + 4] == WHITE):
                    return True

    for row in range(1,ROWS - 5):
        for col in range(1,COLUMNS-1):
            if (BOARD[row][col] == WHITE and
                BOARD[row + 1][col] ==WHITE and
                BOARD[row + 2][col] ==WHITE and
                BOARD[row + 3][col] ==WHITE and
                BOARD[row + 4][col] ==WHITE):
                    return True

    for row in range(1,ROWS - 5):
        for col in range(1,COLUMNS - 5):
            if (BOARD[row][col] == WHITE and
                BOARD[row + 1][col + 1] == WHITE and
                BOARD[row + 2][col + 2] == WHITE and
                BOARD[row + 3][col + 3] == WHITE and
                BOARD[row + 4][col + 4] == WHITE):
                    return True

    for row in range(5, ROWS):
        for col in range(1,COLUMNS - 5):
            if (BOARD[row][col] == WHITE and
                BOARD[row -1 ][col + 1] == WHITE and
                BOARD[row -2][col + 2] == WHITE and
                BOARD[row -3][col + 3] ==WHITE and
                BOARD[row -4][col + 4] == WHITE ):
                    return True

    return False

def numberOfWhiteConn():

    #TWO CONNECTED

    # Check horizontal winning
    for row in range(1, ROWS - 1):
        for col in range(1, COLUMNS - 2):
            if (BOARD[row][col] == WHITE and
                    BOARD[row][col + 1] == WHITE and
                    BOARD[row][col + 2] == ""
                    ):
                #print("Two Connected")
                twoWConnected=True


    for row in range(1, ROWS - 3):
        for col in range(1, COLUMNS - 1):
            if (BOARD[row][col] == WHITE and
                    BOARD[row + 1][col] == WHITE and
                    BOARD[row + 2][col] == ""
                    ):
                #print("Two Connected")
                twoWConnected = True

    for row in range(1, ROWS - 3):
        for col in range(1, COLUMNS - 3):
            if (BOARD[row][col] == WHITE and
                    BOARD[row + 1][col + 1] == WHITE and
                    BOARD[row + 2][col + 2] == ""
                    ):
                #print("Two Connected")
                twoWConnected = True

    for row in range(3, ROWS):
        for col in range(1, COLUMNS - 3):
            if (BOARD[row][col] == WHITE and
                    BOARD[row - 1][col + 1] == WHITE and
                    BOARD[row - 2][col + 2] == ""
                    ):
                #print("Two Connected")
                twoWConnected = True


#Three W connected

# Check horizontal winning
    for row in range(1,ROWS-1):
        for col in range(1,COLUMNS - 4):
            if (BOARD[row][col] ==WHITE and
                BOARD[row][col + 1] == WHITE and
                BOARD[row][col + 2] == WHITE and
                BOARD[row][col + 3] == ""
            ):
                #print("Three Connected")
                threeWConnected = True

    for row in range(1,ROWS - 4):
        for col in range(1,COLUMNS-1):
            if (BOARD[row][col] == WHITE and
                BOARD[row + 1][col] ==WHITE and
                BOARD[row + 2][col] ==WHITE and
                BOARD[row + 3][col] ==""
            ):
                #print("Three Connected")
                threeWConnected = True

    for row in range(1,ROWS - 4):
        for col in range(1,COLUMNS - 4):
            if (BOARD[row][col] == WHITE and
                BOARD[row + 1][col + 1] == WHITE and
                BOARD[row + 2][col + 2] == WHITE and
                BOARD[row + 3][col + 3] == ""
                ):
                #print("Three Connected")
                threeWConnected = True

    for row in range(4, ROWS):
        for col in range(1,COLUMNS - 4):
            if (BOARD[row][col] == WHITE and
                BOARD[row -1 ][col + 1] == WHITE and
                BOARD[row -2][col + 2] == WHITE and
                BOARD[row -3][col + 3] == ""
            ):
                #print("Three Connected")
                threeWConnected = True


# FOUR W CONNECTED

        # Check horizontal winning
        for row in range(1, ROWS - 1):
            for col in range(1, COLUMNS - 5):
                if (BOARD[row][col] == WHITE and
                        BOARD[row][col + 1] == WHITE and
                        BOARD[row][col + 2] == WHITE and
                        BOARD[row][col + 3] == WHITE and
                        BOARD[row][col + 4] == ""
                ):
                    #print("Four Connected")
                    fourWConnected = True

        for row in range(1, ROWS - 5):
            for col in range(1, COLUMNS - 1):
                if (BOARD[row][col] == WHITE and
                        BOARD[row + 1][col] == WHITE and
                        BOARD[row + 2][col] == WHITE and
                        BOARD[row + 3][col] == WHITE and
                        BOARD[row + 4][col] == ""
                ):
                    #print("Four Connected")
                    fourWConnected = True

        for row in range(1, ROWS - 5):
            for col in range(1, COLUMNS - 5):
                if (BOARD[row][col] == WHITE and
                        BOARD[row + 1][col + 1] == WHITE and
                        BOARD[row + 2][col + 2] == WHITE and
                        BOARD[row + 3][col + 3] == WHITE and
                        BOARD[row + 4][col + 4] == ""
                ):
                    #print("Four Connected")
                    fourWConnected = True

        for row in range(5, ROWS):
            for col in range(1, COLUMNS - 5):
                if (BOARD[row][col] == WHITE and
                        BOARD[row - 1][col + 1] == WHITE and
                        BOARD[row - 2][col + 2] == WHITE and
                        BOARD[row - 3][col + 3] == WHITE and
                        BOARD[row - 4][col + 4] == ""
                ):
                    #print("Four Connected")
                    fourWConnected = True


def numberOfBlackConn():
    # TWO CONNECTED

    # Check horizontal winning
    for row in range(1, ROWS - 1):
        for col in range(1, COLUMNS - 3):
            if (BOARD[row][col] == BLACK and
                BOARD[row][col + 1] == BLACK and
                BOARD[row][col + 2] == ""
            ):

                twoBConnected = True

    for row in range(1, ROWS - 3):
        for col in range(1, COLUMNS - 1):
            if (BOARD[row][col] == BLACK and
                BOARD[row + 1][col] == BLACK and
                BOARD[row + 2][col] == ""
            ):

                twoBConnected = True

    for row in range(1, ROWS - 3):
        for col in range(1, COLUMNS - 3):
            if (BOARD[row][col] == BLACK and
                    BOARD[row + 1][col + 1] == BLACK and
                    BOARD[row + 2][col + 2] == ""
            ):

                twoBConnected = True

    for row in range(3, ROWS):
        for col in range(1, COLUMNS - 3):
            if (BOARD[row][col] == BLACK and
                    BOARD[row - 1][col + 1] == BLACK and
                    BOARD[row - 2][col + 2] == ""
            ):

                twoBConnected = True

    # Three B connected

    # Check horizontal winning
    for row in range(1, ROWS - 1):
        for col in range(1, COLUMNS - 4):
            if (BOARD[row][col] == BLACK and
                BOARD[row][col + 1] == BLACK and
                BOARD[row][col + 2] == BLACK and
                BOARD[row][col + 3] == "" ):
                #print("Three BLACK Connected")
                threeBConnected = True

    for row in range(1, ROWS - 4):
        for col in range(1, COLUMNS - 1):
            if (BOARD[row][col] == BLACK and
                    BOARD[row + 1][col] == BLACK and
                    BOARD[row + 2][col] == BLACK and
                    BOARD[row + 3][col] == ""):
                #print("Three BLACK Connected")
                threeBConnected = True

    for row in range(1, ROWS - 4):
        for col in range(1, COLUMNS - 4):
            if (BOARD[row][col] == BLACK and
                    BOARD[row + 1][col + 1] == BLACK and
                    BOARD[row + 2][col + 2] == BLACK and
                    BOARD[row + 3][col + 3] == ""
            ):
                #print("Three BLACK Connected")
                threeBConnected = True

    for row in range(3, ROWS):
        for col in range(1, COLUMNS - 3):
            if (BOARD[row][col] == BLACK and
                    BOARD[row - 1][col + 1] == BLACK and
                    BOARD[row - 2][col + 2] == BLACK and
                    BOARD[row - 3][col + 3] == ""
            ):
                #print("Three BLACK Connected")
                threeBConnected = True

        # FOUR W CONNECTED

        # Check horizontal winning
        for row in range(1, ROWS - 1):
            for col in range(1, COLUMNS - 5):
                if (BOARD[row][col] == BLACK and
                        BOARD[row][col + 1] == BLACK and
                        BOARD[row][col + 2] == BLACK and
                        BOARD[row][col + 3] == BLACK and
                        BOARD[row][col + 4] == ""
                ):
                    #print("Four BLACK Connected")
                    fourBConnected = True

        for row in range(1, ROWS - 5):
            for col in range(1, COLUMNS - 1):
                if (BOARD[row][col] == BLACK and
                        BOARD[row + 1][col] == BLACK and
                        BOARD[row + 2][col] == BLACK and
                        BOARD[row + 3][col] == BLACK and
                        BOARD[row + 4][col] == ""
                ):
                    #print("Four BLACK Connected")
                    fourBConnected = True

        for row in range(1, ROWS - 5):
            for col in range(1, COLUMNS - 5):
                if (BOARD[row][col] == BLACK and
                        BOARD[row + 1][col + 1] == BLACK and
                        BOARD[row + 2][col + 2] == BLACK and
                        BOARD[row + 3][col + 3] == BLACK and
                        BOARD[row + 4][col + 4] == ""
                ):
                    #print("Four BLACK Connected")
                    fourBConnected = True

        for row in range(5, ROWS):
            for col in range(1, COLUMNS - 5):
                if (BOARD[row][col] == BLACK and
                        BOARD[row - 1][col + 1] == BLACK and
                        BOARD[row - 2][col + 2] == BLACK and
                        BOARD[row - 3][col + 3] == BLACK and
                        BOARD[row - 4][col + 4] == ""
                ):
                    #print("Four BLACK Connected")
                    fourBConnected = True



def EvaluateFunction():

    twoWConnected = False
    threeWConnected = False
    fourWConnected = False
    twoBConnected = False
    threeBConnected = False
    fourBConnected = False


    numberOfBlackConn()
    numberOfWhiteConn()




    if winnerIsWhite()==True:
        return 5
    elif winnerIsBlack()==True:
        return -5
    elif fourWConnected == True:
        return 4
    elif threeWConnected == True:
        return 3
    elif twoWConnected == True:
        return 2
    elif fourBConnected == True:
        return -4
    elif threeBConnected == True:
        return -3
    elif twoBConnected == True:
        return -2

    else:
        return 0


def minimax(board, depth, maximizingPlayer):
    if depth == 0 or winnerIsWhite() or winnerIsBlack():
        return EvaluateFunction(), board  # Return the evaluation value and the current board state

    if maximizingPlayer:
        maxEval = float('-inf')
        bestMove = None
        moves = availableSpots()
        for move in moves:
            tempBoard = copy.deepcopy(board)
            tempBoard[move[0]][move[1]] = WHITE
            evaluation = minimax(tempBoard, depth - 1, False)[0]
            if evaluation >= maxEval:
                maxEval = evaluation
                bestMove = tempBoard

        return maxEval, bestMove

    else:
        minEval = float('inf')
        bestMove = None
        moves = availableSpots()
        for move in moves:
            tempBoard = copy.deepcopy(board)
            tempBoard[move[0]][move[1]] = BLACK
            evaluation = minimax(tempBoard, depth - 1, True)[0]
            if evaluation <= minEval:
                minEval = evaluation
                bestMove = tempBoard

        return minEval, bestMove



def Game_Over(emptySpots):
    if emptySpots==0:
        print("Game over!")
        exit()

if __name__ == "__main__":

#declaring the border of the board ABDEFGH for upper and lower and 1-8 for left and right A=65 in ascii
    for i in range(ROWS):
        if (i==0 or i==9):
            pass
        else:
            BOARD[0][i]=chr(65+i-1)
            BOARD[9][i]=chr(65+i-1)
            BOARD[ROWS-i-1][0]=i
            BOARD[ROWS-i-1][9]=i



    while True:

        printMenu()
        choice=int(input("Please choose a game mode: "))
        if choice == 1:
            PLAYER = BLACK
            printBoard(BOARD)
            while True:
                result = playAMove()
                row=result[0]
                column=result[1]
                if BOARD[row][column] != "":
                    print("BAD MOVE!")
                else:
                    if column != 1 and column != 8 and (BOARD[row][column - 1] != "" or BOARD[row][column + 1] != ""):

                        BOARD[row][column] = PLAYER
                        blankSpots = len(emptySpots()) - 1
                        # print(len(emptySpots())-1)
                        changeTurn()
                        printBoard(BOARD)
                        #print(availableSpots())
                        if(winnerIsBlack()):
                            print("BLACK WON THE GAME, GG!")
                            exit()
                        if (winnerIsWhite()):
                            print("BLACK WON THE GAME, GG!")
                            exit()
                        Game_Over(int(blankSpots))



                    elif column < 5:
                        for index, tempColumn in enumerate(BOARD[row][1:(column + 1)], start=1):
                            if (tempColumn == "" and index != column) :
                                print("BAD MOVE!")
                                break
                            elif (index == column) :
                                BOARD[row][column] = PLAYER
                                blankSpots = len(emptySpots()) - 1
                                #print(len(emptySpots())-1)
                                changeTurn()
                                printBoard(BOARD)
                                #print(availableSpots())
                                if (winnerIsBlack()):
                                    print("BLACK WON THE GAME, GG!")
                                    exit()
                                if (winnerIsWhite()):
                                    print("BLACK WON THE GAME, GG!")
                                    exit()
                                Game_Over(int(blankSpots))


                    else:

                        for tempColumn in range(8, (column - 1), -1):
                            #print(tempColumn)
                            if (BOARD[row][tempColumn]== "" and tempColumn != column):
                                print("BAD MOVE!")
                                break
                            elif (tempColumn == column):
                                BOARD[row][column] = PLAYER
                                blankSpots=len(emptySpots()) - 1
                                changeTurn()
                                printBoard(BOARD)
                                #print(availableSpots())
                                if (winnerIsBlack()):
                                    print("BLACK WON THE GAME, GG!")
                                    exit()
                                if (winnerIsWhite()):
                                    print("BLACK WON THE GAME, GG!")
                                    exit()
                                Game_Over(int(blankSpots))




        elif choice == 2:
            printBoard(BOARD)
            while True:
                if PLAYER==BLACK:
                    result = playAMove()
                    row = result[0]
                    column = result[1]
                    if BOARD[row][column] != "":
                        print("BAD MOVE!")
                    else:
                        if column != 1 and column != 8 and (
                                BOARD[row][column - 1] != "" or BOARD[row][column + 1] != ""):

                            BOARD[row][column] = PLAYER
                            blankSpots = len(emptySpots()) - 1
                            # print(len(emptySpots())-1)
                            changeTurn()
                            printBoard(BOARD)
                            #print(availableSpots())
                            if (winnerIsBlack()):
                                print("BLACK WON THE GAME, GG!")
                                exit()
                            if (winnerIsWhite()):
                                print("BLACK WON THE GAME, GG!")
                                exit()
                            Game_Over(int(blankSpots))



                        elif column < 5:
                            for index, tempColumn in enumerate(BOARD[row][1:(column + 1)], start=1):
                                if (tempColumn == "" and index != column):
                                    print("BAD MOVE!")
                                    break
                                elif (index == column):
                                    BOARD[row][column] = PLAYER
                                    blankSpots = len(emptySpots()) - 1
                                    # print(len(emptySpots())-1)
                                    changeTurn()
                                    printBoard(BOARD)
                                    #print(availableSpots())
                                    if (winnerIsBlack()):
                                        print("BLACK WON THE GAME, GG!")
                                        exit()
                                    if (winnerIsWhite()):
                                        print("BLACK WON THE GAME, GG!")
                                        exit()
                                    Game_Over(int(blankSpots))


                        else:

                            for tempColumn in range(8, (column - 1), -1):
                                # print(tempColumn)
                                if (BOARD[row][tempColumn] == "" and tempColumn != column):
                                    print("BAD MOVE!")
                                    break
                                elif (tempColumn == column):
                                    BOARD[row][column] = PLAYER
                                    blankSpots = len(emptySpots()) - 1
                                    changeTurn()
                                    printBoard(BOARD)
                                    #print(availableSpots())
                                    if (winnerIsBlack()):
                                        print("BLACK WON THE GAME, GG!")
                                        exit()
                                    if (winnerIsWhite()):
                                        print("BLACK WON THE GAME, GG!")
                                        exit()
                                    Game_Over(int(blankSpots))


                else:
                    print("[PLAYER 2] IS THINKING......")
                    value,aiMove= minimax(BOARD,3,True)
                    BOARD=aiMove
                    changeTurn()
                    printBoard(BOARD)
                    if (winnerIsBlack()):
                        print("BLACK WON THE GAME, GG!")
                        exit()
                    if (winnerIsWhite()):
                        print("WHITE WON THE GAME, GG!")
                        exit()
                    Game_Over(int(blankSpots))



        elif choice == 3:
            PLAYER = WHITE
            blankSpots = len(emptySpots()) - 1
            printBoard(BOARD)
            while True:
                if PLAYER == BLACK:
                    result = playAMove()
                    row = result[0]
                    column = result[1]
                    if BOARD[row][column] != "":
                        print("BAD MOVE!")
                    else:
                        if column != 1 and column != 8 and (
                                BOARD[row][column - 1] != "" or BOARD[row][column + 1] != ""):

                            BOARD[row][column] = PLAYER
                            blankSpots = len(emptySpots()) - 1
                            # print(len(emptySpots())-1)
                            changeTurn()
                            printBoard(BOARD)
                            # print(availableSpots())
                            if (winnerIsBlack()):
                                print("BLACK WON THE GAME, GG!")
                                exit()
                            if (winnerIsWhite()):
                                print("BLACK WON THE GAME, GG!")
                                exit()
                            Game_Over(int(blankSpots))



                        elif column < 5:
                            for index, tempColumn in enumerate(BOARD[row][1:(column + 1)], start=1):
                                if (tempColumn == "" and index != column):
                                    print("BAD MOVE!")
                                    break
                                elif (index == column):
                                    BOARD[row][column] = PLAYER
                                    blankSpots = len(emptySpots()) - 1
                                    # print(len(emptySpots())-1)
                                    changeTurn()
                                    printBoard(BOARD)
                                    # print(availableSpots())
                                    if (winnerIsBlack()):
                                        print("BLACK WON THE GAME, GG!")
                                        exit()
                                    if (winnerIsWhite()):
                                        print("BLACK WON THE GAME, GG!")
                                        exit()
                                    Game_Over(int(blankSpots))


                        else:

                            for tempColumn in range(8, (column - 1), -1):
                                # print(tempColumn)
                                if (BOARD[row][tempColumn] == "" and tempColumn != column):
                                    print("BAD MOVE!")
                                    break
                                elif (tempColumn == column):
                                    BOARD[row][column] = PLAYER
                                    blankSpots = len(emptySpots()) - 1
                                    changeTurn()
                                    printBoard(BOARD)
                                    # print(availableSpots())
                                    if (winnerIsBlack()):
                                        print("BLACK WON THE GAME, GG!")
                                        exit()
                                    if (winnerIsWhite()):
                                        print("BLACK WON THE GAME, GG!")
                                        exit()
                                    Game_Over(int(blankSpots))


                else:
                    print("[PLAYER 2] IS THINKING......")
                    value, aiMove = minimax(BOARD, 3, True)
                    BOARD = aiMove
                    changeTurn()
                    printBoard(BOARD)
                    if (winnerIsBlack()):
                        print("BLACK WON THE GAME, GG!")
                        exit()
                    if (winnerIsWhite()):
                        print("WHITE WON THE GAME, GG!")
                        exit()
                    Game_Over(int(blankSpots))

        elif choice == 4:
            print("CYAA !!!")
            exit()
        else:
            print("Wrong Input!!")



