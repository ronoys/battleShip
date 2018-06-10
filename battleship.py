#import the module

import Tkinter as tk
import random
import sys

# Basic gameboard setup
class GameBoard(tk.Frame):
    def __init__(self, parent, rows=10, columns=10, size=32, color1="white", color2="black"): # sets board attributes
        

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        self.canvas.bind("<Configure>", self.refresh)

    def addpiece(self, name, image, row, column): # procedure to add pieces to board

        self.canvas.create_image(0,0, image=image, tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)
        

    def placepiece(self, name, row, column): # procedure to place pieces
        
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

    def refresh(self, event): # redraw the board if resized
        
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")



def battleship():
        
    x = 0 # new var
    new_list = [] # list to record the ships
    hit_list = [] # list to record the hits
    miss_list = [] # list to record the misses
    
    while x < 10: # generates series of ten random points for ships
        ship_position = random.randint(0,100)
        ship_row = int(ship_position % 10)
        ship_column = int((ship_position - ship_row) % 9)
        
        if (ship_row,ship_column) in new_list: # if the ship is already placed
            break # exit 
        else:
            new_list.append((ship_row, ship_column)) # otherwise add it to the list
        x = x + 1 # increment variable

    print("Welcome to Battleship. You will be prompted to enter rows and columns. Guess correctly to try and sink all ships before you run out of guesses! In between guesses, close the tk window to continue. ")
    
    
    print ("Cheat mode enabled, here are the locations: ", new_list)
    guesses = 20 # number of guesses

    # while guesses still remaining
    while guesses > 0:
        guess_row = (input("Enter a row guess: ")) # inputs row
        guess_column = input("Enter a column guess: ") # inputs column

        
        # if the guess is a ship, print hit and add it to the board
        if(guess_row, guess_column) in new_list: 
            print("You have gotten a hit")
            hit_list.append((guess_row, guess_column))
            new_list.pop(new_list.index((guess_row,guess_column)))

            root = tk.Tk()
            board = GameBoard(root)
            board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
            player1 = tk.PhotoImage(file='x.gif')
            player2 = tk.PhotoImage(file = 'o.gif')
            for x in hit_list:
                board.addpiece("player" + str(x[0])+ str(x[1]), player1, x[0], x[1])
            for x in miss_list:
                board.addpiece("player" + str(x[0])+ str(x[1]), player2, x[0], x[1])
            root.mainloop()
        

        # if the guess was already guessed, display that
        elif (guess_row, guess_column) in hit_list or (guess_row, guess_column) in miss_list:
            print("You already guessed that.")

        # else print miss and add it to the board               
        else:
            
            print("Miss!")
            miss_list.append((guess_row, guess_column))

            
            root = tk.Tk()
            board = GameBoard(root)
            board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
            player1 = tk.PhotoImage(file='x.gif')
            player2 = tk.PhotoImage(file = 'o.gif')
            for x in hit_list:
                
                board.addpiece("player" + str(x[0])+ str(x[1]), player1, x[0], x[1])
            for x in miss_list:
                
                board.addpiece("player" + str(x[0])+ str(x[1]), player2, x[0], x[1])
            root.mainloop()
            
            
        # increment guesses
        guesses = guesses - 1

        # if no ships remain, print that you won
        if len(new_list) == 0:
            print("You won!")
            break

        # if you run out of guesses, print that you lose
        if guesses == 0:
            print("Sorry you have lost")
            break
    
    
battleship() # call procedure



