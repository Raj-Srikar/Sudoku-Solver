import SudokuFuncs as sf

def main():
    sudoku_matrix = [
                ['1', '5', '-', '8', '-', '-', '7', '-', '2'],
                ['-', '3', '-', '-', '5', '-', '-', '-', '-'],
                ['-', '-', '7', '2', '-', '-', '5', '-', '-'],
                ['-', '-', '-', '-', '-', '1', '-', '9', '-'],
                ['-', '2', '-', '-', '8', '9', '-', '-', '-'],
                ['9', '-', '-', '-', '-', '-', '1', '8', '-'],
                ['3', '6', '-', '-', '-', '2', '-', '-', '4'],
                ['-', '-', '4', '-', '6', '-', '9', '-', '-'],
                ['-', '9', '-', '-', '-', '-', '-', '6', '1']
             ]
    print('Choose an option:')
    print('1. From the file "sample.txt"\n2. Enter manually\n3. From the variable')
    inputType = input()

    print('Choose an option:')
    print('1. Print the solution\n2. Assign solution to a variable')
    outputType = input()

    print('Show time taken (y/n)')
    time = input()
    if time == 'y': showTime = True
    else: showTime = False

    if inputType == '1' and outputType == '1':                          # From the file 'sample.txt'
        sf.solveSudoku('sample.txt', True, showTime)
    elif inputType == '1' and outputType != '1':
        solved = sf.solveSudoku('sample.txt', showTime = showTime)
        print('\n***Stored in a variable***\n')
        for i in solved:
            print(i)

    elif inputType == '2' and outputType == '1':                        # Prompt the sudoku
        sf.solveSudoku(showResults = True , showTime = showTime)
    elif inputType == '2' and outputType != '1':
        solved = sf.solveSudoku(showTime = showTime)
        print('\n***Stored in a variable***\n')
        for i in solved:
            print(i)

    elif inputType == '3' and outputType == '1':                        # From the variable
        sf.solveSudoku(showResults = True , showTime = showTime, matrix = sudoku_matrix)
    elif inputType == '3' and outputType != '1':
        solved = sf.solveSudoku(showTime = showTime, matrix = sudoku_matrix)
        print('\n***Stored in a variable***\n')
        for i in solved:
            print(i)


if __name__ == '__main__':
    main()
