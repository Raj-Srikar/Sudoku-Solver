# SudokuFuncs.py

Contains all the necessary functions required to solve Sudoku.

## Functions

**all_combinations(li)**
    Intitializes the 'combo_recursion' function, which will append the final list to the list, 'return_list'

    args:
    -li - list, of which the combinations will be determined

    returns: list, 'return_list' which contains lists of all the possible combinations of 'li' list

**block_number(row, column)**
    Determines the block number in which the given row and column numbers intersects in sudoku

    args:
    -rows - Row number
    -column - Column number

    returns: Block number

**blockify(sudoku)**
    Converts 9x9 sudoku list into a list containing lists of values in given sudoku's blocks

    args:
    -sudoku - 9x9 sudoku list

    returns: List with lists of values of sudoku blocks

**blocks_has_duplicates(sudoku)**
    Checks whether the given sudoku's blocks have duplicate values or not

    args:
    -sudoku - List containing 3 or 6 or 9 number of lists of sudoku rows

    returns: False if the given blocks have unique values. Else returns True

**combo_recursion(li1, li2)**
    Recursion function used to calculate all the combinations of a list
    (incomplete function, continued in 'all_combinations' function)

    args:
    -li1 - list, that decays
    -li2 - list, that grows

    returns: Nothing, but appends the resultant list to the globally declared list, 'return_list'

**get_sudoku(filename)**
    Extracts sudoku from a file

    args:
    -filename - Name of the text file

    returns: List containing 9 lists, each having 9 numbers of type string

**insert_combos(lst, vertical_sudoku, blockified_sudoku, row_index)**
    Tries all combinations of missing elements and inserts to a list and returns it

    args:
    -lst - list containing missing elements
    -vertical_sudoku - List containing lists of columns of the sudoku
                       (Will be passed again as an argument in value_inserts() function)

    returns: List [nx9] containing lists of all combinations of missing elements inside the given list
             (where n is the number of tried combinations)

**list_difference(li1, li2)**
    Difference between two lists

    args:
    -li1 - 1st list
    -li2 - 2nd list

    returns: resulting list after subtraction

**list_duplicates_of(seq, item)**
    Predicts the indexes of duplicate elements inside a list

    args:
    -seq - List containing repeated elements
    -item - Repeated element

    returns: A list containing the index numbers of the duplicate elements inside the list, 'seq'

**list_intersection(li1, li2)**
    Intersection between two lists

    args:
    -li1 - 1st list
    -li2 - 2nd list

    returns: resulting list after the intersection

**prompt_sudoku()**
    Prompts the user about sudoku values and forms a 9x9 list

    returns: List containing 9 lists, each having 9 numbers of type string

**solveSudoku(fileName='', showResults=False, showTime=False, matrix=[])**
    Solves a Sudoku by prompting about sudoku or reading a text file containing the sudoku or by directly
    taking the matrix as an and either shows the solution or returns it. Can also tell the execution time
    (Any one of the arguments 'fileName' and 'matrix' should be given. Else rises ValueError)

    args:
    -fileName - Name of the text file in which sudoku is present (optional)
    -showResults - Prints the solution if set true. Else returns the solution (optional)
    -showTime - Calculates and shows the execution time only if set true (optional)
    -martix - 9x9 sudoku matrix (optional)

    returns: If 'showResults' parameter is given true, it returns the 9x9 solved sudoku list
             Else simply prints the solution

**value_inserts(original_list, list_of_indexes_of_dashes, missing_number_list, vertical_sudoku, blockified_sudoku, row_index)**
    Inserts the missing values inside a list, at a position where the values are missing inside the list

    args:
    -original_list - List with missing values (containing '-' at the position of missing values)
    -list_of_indexes_of_dashes - List containing all the indexes numbers of the dashes in the original_list
    -missing_number_list - List containing numbers that are missing inside the original_list

    returns: original_list, containing the values of missing_number_list, inserted at the positions of dashes

**vertical(hztl)**
    Transpose of a nx9 list

    args:
    -hztl - List, on which the Transpose will be applied

    returns: Transpose of the list, hztl

**vertically_has_duplicates(*lists)**
    Checks whether the given collection of lists have duplicate values at the same indexes or not

    args:
    -*lists - Any number of lists. Must be atleast 2 and they all should have the same lengths

    returns: True if there are duplicate values at the same indexes of the given lists
