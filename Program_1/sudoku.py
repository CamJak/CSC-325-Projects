# Provide your information as the values of these variables:
myName = 'Cameron, Thomas'
myTechID = '10382168'
myTechEmail = 'cjt025' #only your email id omit @latech.edu
###########################################################

import sys
from hashSet import HashSet

def getColumn(matrix, colIndex):
  col = []
  for rowIndex in range(9):
    col.append(matrix[rowIndex][colIndex])
    
  return col

def getSquare(matrix, rowIndex, colIndex):
  square = []
  for i in range(rowIndex, rowIndex+3): 
    for j in range(colIndex,colIndex+3):
        square.append(matrix[i][j])
        
  return square

def getGroups(matrix):
  groups = []
  # get rows
  for i in range(9):
    groups.append(list(matrix[i]))
  # get columns
  for i in range(9):
    groups.append(getColumn(matrix,i))
  # get squares
  # squares are processed left-right, up-down
  for i in range(0,9,3): 
    for j in range(0,9,3):
      groups.append(getSquare(matrix,i,j))     

  return groups

def cardinality(x):
  return len(x)

def rule1(group):
  ### IMPLEMENT THIS FUNCTION ###

  changed = False
  
  # RULE 1 - You have to look for duplicate sets (i.e. set([1,6])). If you 
  # have same number of duplicate sets in a group (row, column, square) as 
  # the cardinality of the duplicate set size, then they must each get one 
  # value from the duplicate set. In this case the values of the duplicate 
  # set may be removed from all the other sets in the group. 

  # check each combination of cells in group
  for pInx in range(9):
    duplicates = []
    for sInx in range(9):
      if group[sInx].issuperset(group[pInx]) and (len(group[sInx]) == len(group[pInx])):
        duplicates.append(sInx)
    if cardinality(group[pInx]) == len(duplicates):
      for tInx in range(9):
        if tInx in duplicates:
          continue
        else:
          old = HashSet(group[tInx])
          group[tInx].difference_update(group[pInx])
          if not (group[tInx].issuperset(old) and (len(group[tInx]) == len(old))):
            changed = True

  return changed
  
def rule2(group):
  ### IMPLEMENT THIS FUNCTION ###

  changed = False
  # RULE 2 - Reduce set size by throwing away elements that appear in other
  # sets in the group

  for pInx in range(9):
    if cardinality(group[pInx]) > 1:
      temp = HashSet(group[pInx])
      for sInx in range(9):
        if pInx == sInx:
          continue
        else:
          temp.difference_update(group[sInx])
      if cardinality(temp) == 1:
        group[pInx].clear()
        group[pInx].update(temp)
        changed = True

  return changed

def reduceGroup(group):
  changed = False 
  # this sorts the sets from smallest to largest based cardinality
  group.sort(key=cardinality)
  changed = rule2(group)
  changed = rule1(group)
  
  return changed

def reduceGroups(groups):
  changed = False
  for group in groups:
    if reduceGroup(group):
      changed = True
      
  return changed

def reduce(matrix):
    changed = True
    groups = getGroups(matrix)
    
    while changed:
        changed = reduceGroups(groups)

def printMatrix(matrix):
  for i in range(9):
    for j in range(9):
      if len(matrix[i][j]) != 1:
        sys.stdout.write("x ")
      else:
        for k in matrix[i][j]:
          sys.stdout.write(str(k) + " ")

    sys.stdout.write("\n")

def main():
  file = open(sys.argv[1], "r")
  matrix = []

  for line in file:
    lst = line.split()
    row = []

    for val in lst:
      if val == 'x':
        s = HashSet(range(1,10))
      else:
        s = HashSet([eval(val)])
      row.append(s)

    matrix.append(row)

  print("Solving this puzzle:")
  printMatrix(matrix)

  reduce(matrix)

  print()
  print("Solution:")
  printMatrix(matrix)
  
main()
