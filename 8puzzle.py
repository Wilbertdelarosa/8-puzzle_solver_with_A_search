""" 
Author of code: Wilbert De la Rosa  | FINAL PROJECT - COMP 4200 AI - FALL 2022
----------------------------------------------------------------------
For this implementation I already have created a final State which is:
    1 2 3
    4 _ 5
    6 7 8

INPUT: User just need to input an intial state and the code will find a solution:
For example:
    1 2 3
    4 5 8
    6 7 _
"""
import numpy as np

#Final state desired
FinalState = [['1','2','3'],
              ['4','_','5'],
              ['6','7','8']]

#Accepts and returns user input of Desire starting state Puzzle
def startPuzzle():
        print("Please insert your Initial state 3x3 matrix: ")
        matrices = []
        for i in range(0,3):
            numbers = input().split(" ")
            matrices.append(numbers)
        print("\n")
        return matrices

##Function that copy the initial matrix-> creates 4 new matrices-> select lowest h(n) matrices out of the 4
def movementsXY(initPuzzle):
    positionOfBlank = []
    for x in range(0,3):
            for y in range(0,3):
                if initPuzzle[x][y] == '_':
                    positionOfBlank.append(x)
                    positionOfBlank.append(y)
   
    return positionOfBlank

#This function copy the current state/matrix 
def copyMatrix(Matrix):
    tempMatrix = []
    for i in Matrix:
        t = []
        for j in i:
            t.append(j)
        tempMatrix.append(t)
    return tempMatrix

#All this functions will swap the blanks to the corresponding position
def right(Matrix, positionOfBlank):
    tempMatrix = copyMatrix(Matrix)

    if positionOfBlank[1] == 0  or positionOfBlank[1] == 1:
        tempPosition = tempMatrix[positionOfBlank[0]][positionOfBlank[1]+1]
        tempMatrix[positionOfBlank[0]][positionOfBlank[1]+1] = '_'
        tempMatrix[positionOfBlank[0]][positionOfBlank[1]] = tempPosition
        
    h = hFunction(tempMatrix,FinalState)
    return tempMatrix, h

def left(Matrix, positionOfBlank):
    tempMatrix = copyMatrix(Matrix)
    if positionOfBlank[1] == 1  or positionOfBlank[1] == 2:
        tempPosition = tempMatrix[positionOfBlank[0]][positionOfBlank[1]-1]
        tempMatrix[positionOfBlank[0]][positionOfBlank[1]-1] = '_'
        tempMatrix[positionOfBlank[0]][positionOfBlank[1]] = tempPosition
        
    h = hFunction(tempMatrix,FinalState)
    return tempMatrix, h

def up(Matrix, positionOfBlank):
    tempMatrix = copyMatrix(Matrix)
    if positionOfBlank[0] == 1  or positionOfBlank[0] == 2:
        tempPosition = tempMatrix[positionOfBlank[0]-1][positionOfBlank[1]]
        tempMatrix[positionOfBlank[0]-1][positionOfBlank[1]] = '_'
        tempMatrix[positionOfBlank[0]][positionOfBlank[1]] = tempPosition
        
    h = hFunction(tempMatrix,FinalState)
    return tempMatrix, h

def down(Matrix, positionOfBlank):
    tempMatrix = copyMatrix(Matrix)
    if positionOfBlank[0] == 0  or positionOfBlank[0] == 1:
        tempPosition = tempMatrix[positionOfBlank[0]+1][positionOfBlank[1]]
        tempMatrix[positionOfBlank[0]+1][positionOfBlank[1]] = '_'
        tempMatrix[positionOfBlank[0]][positionOfBlank[1]] = tempPosition
        
    h = hFunction(tempMatrix,FinalState)
    return tempMatrix, h


#This function counts the h number and will compare the current puzzle against the final
def hFunction(matrix, FinalState):

        h = 0
        for x in range(0,3):
            for y in range(0,3):
                if matrix[x][y] != FinalState[x][y] and matrix[x][y] != '_':
                    h += 1
        return h

#Main function that contains all functions call
def mainFunction():
    #For loop that runs hfunction to get the lowest h of all posible states
    currentState = startPuzzle()
    h = hFunction(currentState,FinalState)
    if h == 0:
        print("Your initial state has reached the goal")
    Dh=1
    Uh=1
    Rh=1 
    Lh=1
    
    while True:
        positionOfBlank = movementsXY(currentState)
        depth = 0
        Dm, Dh = down(currentState, positionOfBlank)
        Um, Uh = up(currentState, positionOfBlank)
        Rm, Rh = right(currentState, positionOfBlank)
        Lm, Lh = left(currentState, positionOfBlank)

        #adds all the matrices to a dictionary
        dictionaryofMatrices = {}
        dictionaryofMatrices[Dh] = Dm
        dictionaryofMatrices[Uh] = Um
        dictionaryofMatrices[Rh] = Rm
        dictionaryofMatrices[Lh] = Lm
        
        #find the mind value of the key and sets the current state as the matrix with the min F(n)
        minval = min(dictionaryofMatrices.keys())
        currentState = dictionaryofMatrices[minval]
        depth=depth+1
        print("next A* state generated:")
        for i in currentState:
                    for j in i:
                        print(j,end=" ")
                    print("")
        
        print("f(n) = ",minval)
        print("\n")
        if minval==0:
            print("FINISH!")
            return None

mainFunction()



