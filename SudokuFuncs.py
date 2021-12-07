import time
import itertools

nums= ['1','2','3','4','5','6','7','8','9']     #Global declaration for numbers in sudoku

def get_sudoku(filename):
    """
    Extracts sudoku from a file

    args:
    -filename - Name of the text file

    returns: List containing 9 lists, each having 9 numbers of type string
    """
    rows=[]
    fh = open(filename)
    for inp in fh:
        elements = []
        for j in inp.rstrip():
            if j=='-' or j not in elements: elements.append(j)
            else: break
        if len(elements)==9:
            rows.append(elements)
        else:
            print("INVALID SUDOKU!")
            quit()
    return rows


def prompt_sudoku():
    """
    Prompts the user about sudoku values and forms a 9x9 list

    returns: List containing 9 lists, each having 9 numbers of type string
    """
    rows = []
    i = 0
    while i<9:
        elements = []
        inp = input()
        for j in inp:
            if j=='-' or j not in elements:
                elements.append(j)
            else: break
        if len(elements)==9:
            rows.append(elements)
            i=i+1
        else:
            print("Please enter 9 unique digits!")
    return rows


def solveSudoku(fileName = "", showResults = False, showTime = False, matrix = []):
    """
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
    """
    if fileName == "" and matrix == []: rows = prompt_sudoku()
    elif fileName != "" and matrix == []: rows = get_sudoku(fileName)
    elif fileName == "" and matrix != []: rows = matrix
    elif fileName != "" and matrix !=[]:  raise ValueError("Please give any of the arguments, 'fileName' or 'matrix' (Both are given)")

    st = time.time()
    all_combo = []
    vert = vertical(rows)
    blocks = blockify(rows)
    for i in rows:
        all_combo.append(insert_combos(i, vert, blocks,rows.index(i)))

    a = all_combo.copy()

    for r1 in a[0]:
        for r2 in a[1]:
            if vertically_has_duplicates(r1,r2): continue
            for r3 in a[2]:
                if vertically_has_duplicates(r1,r2,r3) or blocks_has_duplicates([r1,r2,r3]): continue
                for r4 in a[3]:
                    if vertically_has_duplicates(r1,r2,r3,r4): continue
                    for r5 in a[4]:
                        if vertically_has_duplicates(r1,r2,r3,r4,r5): continue
                        for r6 in a[5]:
                            if vertically_has_duplicates(r1,r2,r3,r4,r5,r6) or blocks_has_duplicates([r1,r2,r3,r4,r5,r6]): continue
                            for r7 in a[6]:
                                if vertically_has_duplicates(r1,r2,r3,r4,r5,r6,r7): continue
                                for r8 in a[7]:
                                    if vertically_has_duplicates(r1,r2,r3,r4,r5,r6,r7,r8): continue
                                    for r9 in a[8]:
                                        try_sol = []
                                        try_sol = [r1,r2,r3,r4,r5,r6,r7,r8,r9]
                                        if vertically_has_duplicates(r1,r2,r3,r4,r5,r6,r7,r8,r9) or blocks_has_duplicates(try_sol): continue
                                        time_taken = 'Time Taken:  '+str(round(time.time()-st, 4))+'s'
                                        if showResults:
                                            for row in try_sol:
                                                print(row)
                                            if showTime: print(time_taken)
                                        else:
                                            if showTime: try_sol.append(time_taken)
                                            return try_sol


def blocks_has_duplicates(sudoku):
    """
    Checks whether the given sudoku's blocks have duplicate values or not

    args:
    -sudoku - List containing 3 or 6 or 9 number of lists of sudoku rows

    returns: False if the given blocks have unique values. Else returns True
    """
    is_correct = True
    blocks = blockify(sudoku)
    for i in blocks:
        if is_correct:
            i.sort()
            is_unique = i==nums
            is_correct = is_correct and is_unique
        else:
            break
    return not is_correct


def blockify(sudoku):
    """
    Converts 9x9 sudoku list into a list containing lists of values in given sudoku's blocks

    args:
    -sudoku - 9x9 sudoku list

    returns: List with lists of values of sudoku blocks
    """
    i=0
    block_row = []
    while i<len(sudoku):
        j=0
        while j<7:
            k=i
            blocked = []
            while k<i+3:
                l=j
                block = []
                while l<j+3:
                    block.append(sudoku[k][l])
                    l += 1
                blocked.extend(block)
                k += 1
            block_row.append(blocked)
            j += 3
        i += 3
    return block_row


def vertically_has_duplicates(*lists):
    """
    Checks whether the given collection of lists have duplicate values at the same indexes or not

    args:
    -*lists - Any number of lists. Must be atleast 2 and they all should have the same lengths

    returns: True if there are duplicate values at the same indexes of the given lists
    """
    rows = list(lists)
    vert = vertical(rows)
    is_not_equal = True
    for i in vert:
        set_row = set(i)
        is_not_equal = is_not_equal and (len(set_row) == len(i))
        if not is_not_equal:
            break
    return not is_not_equal


def list_difference(li1, li2):
    """
    Difference between two lists

    args:
    -li1 - 1st list
    -li2 - 2nd list

    returns: resulting list after subtraction
    """
    li_dif = [i for i in li1 + li2 if i in li1 and i not in li2]
    return li_dif


return_list = []        #Global declaration of the List to be returned after all the combinations are appended to it


def all_combinations(li):
    """
    This will append all combination lists to the list, 'return_list'

    args:
    -li - list, of which the combinations will be determined

    returns: list, 'return_list' which contains lists of all the possible combinations of 'li' list
    """
    return_list.clear()
    combination_in_tuple = list(itertools.permutations(li))
    for i in combination_in_tuple:
        return_list.append(list(i))
    return return_list


def block_number(row, column):
    """
    Determines the block number in which the given row and column numbers intersects in sudoku

    args:
    -rows - Row number
    -column - Column number

    returns: Block number
    """
    ele = str(row) + str(column)
    skeleton_matrix = [
        ['00', '01', '02', '10', '11', '12', '20', '21', '22'],
        ['03', '04', '05', '13', '14', '15', '23', '24', '25'],
        ['06', '07', '08', '16', '17', '18', '26', '27', '28'],
        ['30', '31', '32', '40', '41', '42', '50', '51', '52'],
        ['33', '34', '35', '43', '44', '45', '53', '54', '55'],
        ['36', '37', '38', '46', '47', '48', '56', '57', '58'],
        ['60', '61', '62', '70', '71', '72', '80', '81', '82'],
        ['63', '64', '65', '73', '74', '75', '83', '84', '85'],
        ['66', '67', '68', '76', '77', '78', '86', '87', '88']
    ]
    for i in skeleton_matrix:
        if ele in i:
            return skeleton_matrix.index(i)


def value_inserts(original_list, list_of_indexes_of_dashes, missing_number_list, vertical_sudoku, blockified_sudoku, row_index):
    """
    Inserts the missing values inside a list, at a position where the values are missing inside the list

    args:
    -original_list - List with missing values (containing '-' at the position of missing values)
    -list_of_indexes_of_dashes - List containing all the indexes numbers of the dashes in the original_list
    -missing_number_list - List containing numbers that are missing inside the original_list

    returns: original_list, containing the values of missing_number_list, inserted at the positions of dashes
    """
    i=0
    while i < len(list_of_indexes_of_dashes):
        in_block = missing_number_list[i] in blockified_sudoku[block_number(row_index, list_of_indexes_of_dashes[i])]
        in_column = missing_number_list[i] in vertical_sudoku[list_of_indexes_of_dashes[i]]
        if not in_column and not in_block:
            original_list[list_of_indexes_of_dashes[i]] = missing_number_list[i]
        else:
            return []
        i=i+1
    return original_list


def insert_combos(lst, vertical_sudoku, blockified_sudoku, row_index):
    """
    Tries all combinations of missing elements and inserts to a list and returns it

    args:
    -lst - list containing missing elements
    -vertical_sudoku - List containing lists of columns of the sudoku
                       (Will be passed again as an argument in value_inserts() function)

    returns: List [nx9] containing lists of all combinations of missing elements inside the given list
             (where n is the number of tried combinations)
    """
    rows_combo = []
    missing = list_difference(nums, lst)
    indexes = list_duplicates_of(lst,'-')
    if len(missing) != 1:
        missing_combo = all_combinations(missing)
    else: missing_combo = [missing]
    for i in missing_combo:
        inserted = value_inserts(lst, indexes, i, vertical_sudoku, blockified_sudoku, row_index)
        if len(inserted) != 0:
            rows_combo.append(inserted[:])      # NOTE: Not working without '[:]' at the end of the list, 'inserted'
                                                # REFERENCE: https://stackoverflow.com/questions/5280799/list-append-changing-all-elements-to-the-appended-item
    return rows_combo


def vertical(hztl):
    """
    Transpose of a nx9 list

    args:
    -hztl - List, on which the Transpose will be applied

    returns: Transpose of the list, hztl
    """
    i=0
    vert = []
    while i<9:
        j=0
        ele = []
        while j<len(hztl):
            ele.append(hztl[j][i])
            j=j+1
        vert.append(ele)
        i=i+1
    return vert


def list_duplicates_of(seq, item):
    """
    Predicts the indexes of duplicate elements inside a list

    args:
    -seq - List containing repeated elements
    -item - Repeated element

    returns: A list containing the index numbers of the duplicate elements inside the list, 'seq'
    """
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item, start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs
