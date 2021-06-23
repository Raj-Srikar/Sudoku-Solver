import SudokuFuncs as sf

def main():
    print('Choose an option:')
    print('1. From file "sample.txt"\n2. Enter manually')
    inputType = input()

    print('Choose an option:')
    print('1. Print the solution\n2. Assign solution to a variable')
    outputType = input()

    print('Show time taken (y/n)')
    time = input()
    if time == 'y': showTime = True
    else: showTime = False

    if inputType == '1' and outputType == '1':
        sf.solveSudoku('sample.txt', True, showTime)
    elif inputType == '1' and outputType != '1':
        solved = sf.solveSudoku('sample.txt', showTime = showTime)
        print('Stored in a variable')
        for i in solved:
            print(i)
    elif inputType != '1' and outputType == '1':
        sf.solveSudoku(showResults = True , showTime = showTime)
    elif inputType != '1' and outputType != '1':
        solved = sf.solveSudoku(showTime = showTime)
        print('Stored in a variable')
        for i in solved:
            print(i)


if __name__ == '__main__':
    main()
