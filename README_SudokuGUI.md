# SudokuGUI.py

GUI Implementation of the **Sudoku-Solver**.

## Features of the Application

- Can import Sudoku from a text file.
- Show the time taken to solve.
- Highlight the solved digits.
- Change the highlight color.
- Clear the Sudoku Grid at once.

## Usage of the Application

- Blank sudoku cells can be given as '-' or can be left blank.
- Must provide Sudoku with atleast 25 digits.
- 'Clear' button will clear all the Sudoku Cells.
- 'From File' button is used to import a Sudoku from a text file.
- 'Show Time Taken' check button will show the time taken to solve the given sudoku, if enabled.
- 'Highlight Solved Digits' check button will highlight all the solved digits in Red color by default.
- The color combo box is used to change the highlight color according to our convenience. It contains 'Red', 'Blue', 'Green', 'Orange', 'Purple' colors.
- The 'SOLVE' button will solve the given Sudoku, if it's valid. It almost solves within 10 seconds. (All the experimental test cases took within 7 seconds and never exceeded 10 seconds mark. So I can't say for sure ;)

# Executable File

Run SudokuGUI.exe in your PC.

## Functions in the Code

**clear()**
    Will be called on clicking the 'Clear' Button.

    Clears all the Sudoku Grid Entries

**display_time()**
    Will be called on checking the 'Show Time' Checkbutton.

    Enables and disables the "lbl_time" Label

**from_file()**
    Will be called on clicking the 'From File' Button.

    Invokes askopenfilename dialog and imports the Sudoku from the selected text file and fills up all
    the Entries.

**goto_bottom_entry()**
    Called in the KeyPress() function

    Selects the Entry below on pressing the Down Arrow Key

**goto_next_entry()**
    Called in the KeyPress() function

    Selects the next Entry on pressing the Right Arrow Key

**goto_prev_entry()**
    Called in the KeyPress() function

    Selects the previous Entry on pressing the Left Arrow Key

**goto_top_entry()**
    Called in the KeyPress() function

    Selects the upper Entry on pressing the Up Arrow Key

**highlight(e=0)**
    Will be called on checking the 'Highlight Solved Digits' Checkbutton and on selecting an option in the
    Color Combobox

    Highlights all the solved digits in the Sudoku, by changing their color to the selected color in the
    Color Combobox

**keyPress(event)**
    Bounded to all the Entries in the Sudoku Grid

    Detects the keyPress events while any of the Entries is selected. Allows characters only if it is a
    number or '-' or a space. Also used to navigate through the Entries by detecting the arrow key events

**solve()**
    Will be called on clicking the 'SOLVE' Button.

    Extracts all the digits given in the Sudoku Grid Entries and forms a 9x9 list. Then passes this list as
    an argument while calling the "solveSudoku()" function. After solving, all the entries will be refilled
    again with solved digits.
