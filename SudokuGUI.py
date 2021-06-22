import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename
from SudokuFuncs import solveSudoku, list_duplicates_of
import tkinter.font as font
import time


indexes = []
def solve():
    """
    Will be called on clicking the 'SOLVE' Button.

    Extracts all the digits given in the Sudoku Grid Entries and forms a 9x9 list. Then passes this list as
    an argument while calling the "solveSudoku()" function. After solving, all the entries will be refilled
    again with solved digits.
    """
    try:
        st = time.time()
        rows_extracted = []
        count = 0
        for row in rows:
            columns_extracted = []
            for cell in row:
                cell_text = cell.get()
                if cell_text == '':
                    columns_extracted.append('-')
                else:
                    columns_extracted.append(cell_text)
            count += columns_extracted.count('-')
            rows_extracted.append(columns_extracted)
        if count > 56:
            mb.showwarning('Low Digits Detected', 'Please provide Sudoku with atleast 25 digits!')
            return
        for i in rows_extracted:
            indexes.append(list_duplicates_of(i,'-'))
        solved = solveSudoku(matrix=rows_extracted)
        i=0
        while i<9:
            j=0
            while j<9:
                if rows[i][j].get() != solved[i][j]:
                    rows[i][j].delete(0,tk.END)
                    rows[i][j].insert(0,solved[i][j])
                    if hlght_var.get() == 1:
                        rows[i][j].config({"foreground": "red"})
                j+=1
            i+=1
        time_taken = 'Time Taken: '+str(round(time.time()-st, 2))+'s'
        lbl_time['text'] = time_taken
    except:
        mb.showerror('Error', 'An Unknown error occurred!')


def display_time():
    """
    Will be called on checking the 'Show Time' Checkbutton.

    Enables and disables the "lbl_time" Label
    """
    if time_var.get() == 0:
        lbl_time.grid_forget()
    if time_var.get() == 1:
        lbl_time.grid(row = 1, column = 0, sticky = 'nw', padx = 25, pady = 3)


def highlight(e=0):
    """
    Will be called on checking the 'Highlight Solved Digits' Checkbutton and on selecting an option in the
    Color Combobox

    Highlights all the solved digits in the Sudoku, by changing their color to the selected color in the
    Color Combobox
    """
    if indexes != []:
        i=0
        while i<9:
            for j in indexes[i]:
                if hlght_var.get() == 1:
                    rows[i][j].config({"foreground": color_var.get().lower()})
                elif hlght_var.get() == 0:
                    rows[i][j].config({"foreground": "black"})
            i+=1
    if hlght_var.get() == 1:
        cmb_color['state'] = 'readonly'
    elif hlght_var.get() == 0:
        cmb_color['state'] = 'disabled'
    window.focus()                      #Removing focus from combobox


def goto_next_entry():
    """
    Called in the KeyPress() function

    Selects the next Entry on pressing the Right Arrow Key
    """
    focused_entry = window.focus_get()
    ind = all_entries.index(focused_entry)
    if ind != len(all_entries)-1:
        ind += 1
        all_entries[ind].focus()

def goto_prev_entry():
    """
    Called in the KeyPress() function

    Selects the previous Entry on pressing the Left Arrow Key
    """
    focused_entry = window.focus_get()
    ind = all_entries.index(focused_entry)
    if ind != 0:
        ind -= 1
        all_entries[ind].focus()

def goto_top_entry():
    """
    Called in the KeyPress() function

    Selects the upper Entry on pressing the Up Arrow Key
    """
    focused_entry = window.focus_get()
    ind = all_entries.index(focused_entry)
    if ind > 8:
        ind -= 9
        all_entries[ind].focus()

def goto_bottom_entry():
    """
    Called in the KeyPress() function

    Selects the Entry below on pressing the Down Arrow Key
    """
    focused_entry = window.focus_get()
    ind = all_entries.index(focused_entry)
    if ind < 71:
        ind += 9
        all_entries[ind].focus()


def keyPress(event):
    """
    Bounded to all the Entries in the Sudoku Grid

    Detects the keyPress events while any of the Entries is selected. Allows characters only if it is a
    number or '-' or a space. Also used to navigate through the Entries by detecting the arrow key events
    """
    if event.char in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '-') :
        focused = frm_sudoku.focus_get()
        focused.delete(0,tk.END)
        goto_next_entry()
    elif event.keysym == 'Right':
        goto_next_entry()
    elif event.keysym == 'Left':
        goto_prev_entry()
    elif event.keysym == 'Up':
        goto_top_entry()
    elif event.keysym == 'Down':
        goto_bottom_entry()
    elif event.keysym == 'BackSpace':
        frm_sudoku.focus_get().delete(0,tk.END)
        goto_prev_entry()
    elif event.keysym == 'Delete':
        frm_sudoku.focus_get().delete(0,tk.END)
        goto_next_entry()
    elif event.keysym not in ('Tab', 'Shift_L', 'Shift_R', 'Alt_L', 'F4'):
        print(event.keysym)
        return 'break'


def from_file():
    """
    Will be called on clicking the 'From File' Button.

    Invokes askopenfilename dialog and imports the Sudoku from the selected text file and fills up all
    the Entries.
    """
    chk_highlight.deselect()
    chk_time.deselect()
    lbl_time.grid_forget()
    cmb_color['state'] = 'disabled'
    for i in rows:
        for j in i:
            j.config({"foreground": "black"})
    filepath = askopenfilename(
        filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')]
    )
    if not filepath:
        return
    with open(filepath, 'r') as content:
        indexes.clear()
        raw = content.read()
        lines = raw.split('\n')
        line = 0
        while line < 9:
            letter = 0
            while letter < 9:
                rows[line][letter].delete(0, tk.END)
                rows[line][letter].insert(0, lines[line][letter])
                letter+=1
            line+=1


def clear():
    """
    Will be called on clicking the 'Clear' Button.

    Clears all the Sudoku Grid Entries
    """
    indexes.clear()
    lbl_time.config(text = '')
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            rows[i][j].delete(0,tk.END)
            rows[i][j].config({"foreground": "black"})
            j += 1
        i += 1


window = tk.Tk()                                                                # Tkinter Window definition
window.title('Sudoku Solver')
window.configure(bg = '#15a6d6')


window.rowconfigure(1, minsize = 550)
window.columnconfigure(0, minsize = 600)
window.columnconfigure(1, minsize = 150)

frm_main = tk.Frame(window, bg = '#15a6d6')                                     # Main frame that contains the Sudoku frame and the 2 buttons below
frm_main.rowconfigure(0, minsize = 600)
frm_main.rowconfigure(1, minsize = 50)
frm_main.columnconfigure(0, minsize = 600)
frm_sudoku = tk.Frame(frm_main, relief = tk.RIDGE, bd = 5, bg = '#e8e26d')      # Frame that holds Sudoku grid
frm_solve = tk.Frame(window, bg = '#15a6d6')                                    # Frame that holds the 'Solve' button and other things on the right

cnv = tk.Canvas(frm_sudoku,                                                     # For creating the Sudoku grid lines and placing them manually
                bg = '#e8e26d',
                highlightthickness = 0,
                bd = 0,
                width = 550,
                height = 565
                )
cnv.create_line(0,190,550,190, width = 2)
cnv.create_line(180,0,180,565, width = 2)
cnv.create_line(0,380,550,380, width = 2)
cnv.create_line(360,0,360,565, width = 2)
cnv.place(x=0,y=0)

rows = []                                           # List to store 9 row lists that contains Tkinter Entries
i=0
while i < 9:
    j=0
    single_row = []                                 # List to store Tkinter Entries, present as an individual row
    while j < 9:
        if j == 0 or j == 3 or j == 6:              # For setting x padding accordingly
            x = (20,10)
        elif j == 2 or j == 5 or j == 8:
            x = (10,20)
        else:
            x = 10

        if i == 0 or i == 3 or i == 6:              # For setting y padding accordingly
            y = (20,10)
        elif i == 2 or i == 5 or i == 8:
            y = (10,20)
        else:
            y = 10
        ent_cell = tk.Entry(                        # Entry Cell definition
            frm_sudoku,
            font = "Helvetica 20 bold",
            width = 2,
            justify = 'center',
            highlightbackground="black",
            highlightcolor="red",
            highlightthickness=1,
            bd=0
        )
        ent_cell.bind('<KeyPress>', keyPress)
        ent_cell.grid(row = i, column = j, padx = x, pady = y)
        single_row.append(ent_cell)                 # Storing 9 Entry Cells in the list single_row
        j+=1
    rows.append(single_row)                         # Storing 9 1ists containing Entry Cells in the list rows
    i+=1

all_entries = [ent for row in rows for ent in row]                              # Storing all the Entry Cells individually in a single list
all_entries[0].focus()                                                          # Focus the first Entry

lbl_title = tk.Label(window,                        # Title Label
                     text = 'Sudoku Solver',
                     bg = '#15a6d6',
                     fg = 'black',
                     font = ('Comic Sans MS',
                              45,
                              'bold',
                              'italic'
                              )
                     )
fnt_solve = font.Font(family='Times New Roman', size=14, weight='bold')         # Font for 'Solve' button
fnt_fc = font.Font(family='Helvetica', size=11)                                 # Font for 'From File' and 'Clear' buttons

lbl_time = tk.Label(frm_main,                       # Time Label
                    bg = '#15a6d6',
                    fg = '#31115e',
                    font = ('Times New Roman bold',15))

btn_file = tk.Button(frm_main,                      # 'From File' button
                     text = 'From File',
                     width = 8,
                     height = 1,
                     bg = '#cb80e8',
                     activebackground = '#b676cf',
                     font = fnt_fc,
                     command = from_file
                     )
btn_clear = tk.Button(frm_main,                     # 'Clear' button
                      text = 'Clear',
                      width = 8,
                      height = 1,
                      bg = '#cb80e8',
                      activebackground = '#b676cf',
                      font = fnt_fc,
                      command = clear
                      )

btn_solve = tk.Button(frm_solve,                    # 'Solve' button
                      text = 'SOLVE',
                      width  = 10,
                      height = 2,
                      bg = '#80dee8',
                      activebackground = '#6fc8d1',
                      font = fnt_solve,
                      command = solve
                      )

time_var = tk.IntVar()
chk_time = tk.Checkbutton(frm_solve,                                            # Checkbutton to show time taken to solve the Sudoku
                          text = 'Show Time Taken',
                          variable = time_var,
                          onvalue = 1,
                          offvalue = 0,
                          bg = '#15a6d6',
                          activebackground= '#15a6d6',
                          command = display_time
                          )

hlght_var = tk.IntVar()
chk_highlight = tk.Checkbutton(frm_solve,                                       # Checkbutton to highlight the solved digits in the Sudoku grid
                               text = 'Highlight Solved Digits',
                               variable = hlght_var,
                               onvalue = 1,
                               offvalue = 0,
                               bg = '#15a6d6',
                               activebackground= '#15a6d6',
                               command = highlight
                               )

color_var = tk.StringVar()
cmb_color = ttk.Combobox(frm_solve,                                             # Combobox to select the color, in which the digits should be highlighted
                         textvariable = color_var,
                         state = 'disabled',
                         width = 17
                         )
cmb_color['values'] = ('Red',
                       'Blue',
                       'Green',
                       'Orange',
                       'Purple',
                        )
cmb_color.current(0)
cmb_color.bind('<<ComboboxSelected>>', highlight)

lbl_creds = tk.Label(window,                        # Credit Label
                     text = 'By - Raj Srikar',
                     bg = '#15a6d6',
                     font = ('Comic Sans MS',10))

lbl_title.grid(row = 0, column = 0, columnspan = 2, sticky = 'ew', pady = (5,0))                # Placing the Title Label in the grid
frm_main.grid(row = 1, column = 0, sticky = 'nsew')                                             # Placing the Main Frame in the grid
frm_sudoku.grid(row = 0, column = 0, sticky = 'nsew', padx = 20, pady = 15)                     # Placing the Sudoku Framein the grid
frm_solve.grid(row = 1, column = 1)                                                             # Placing the Solve button Framein the grid
btn_clear.grid(row = 1, column = 0, sticky = 'ne', padx = 110)                                  # Placing the 'Clear' button in the grid
btn_file.grid(row = 1, column = 0, sticky = 'ne', padx = 20)                                    # Placing the 'From File' button in the grid
btn_solve.grid(row = 0, column = 0, padx = (15,35))                                             # Placing the 'Solve' button in the grid
chk_time.grid(row = 1, column = 0, pady = (20,0), padx = 10, sticky = 'w')                      # Placing the Time Checkbutton in the grid
chk_highlight.grid(row = 2, column = 0, pady = (5,5))                                           # Placing the Highlight Checkbutton in the grid
cmb_color.grid(row = 3, column = 0, sticky = 'e', padx = 15)                                    # Placing the Color Combobox in the grid
lbl_creds.grid(row = 2, column = 0, columnspan = 2, sticky = 'e', padx = 5, pady = (0,5))       # Placing the Credit Label in the grid

window.eval('tk::PlaceWindow . center')                                         # To position the window in the center of the screen
window.mainloop()                                                               # You know what this is x)
