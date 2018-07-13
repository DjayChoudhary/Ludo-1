import tkinter as tk
import time

from settings import *
from board import *
from coin import *

def align(x, y, color):
    list = []
    for i in range(2):
        test = Coin(ludo.get_canvas(), x, y + i*2*Board.SQUARE_SIZE, color=color, coin_index=i)
        list.append(test)
    for i in range(2):
        test = Coin(ludo.get_canvas(), x + 2*Board.SQUARE_SIZE, y + i*2*Board.SQUARE_SIZE, color=color, coin_index=i+2)
        list.append(test)
    return list

root = tk.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('{}x{}'.format(width, height))
root.title('Ludo')

ludo = LudoBoard(root)
ludo.create()
green = align(2*Board.SQUARE_SIZE, 2*Board.SQUARE_SIZE, color='green')
red = align(2*Board.SQUARE_SIZE, 11*Board.SQUARE_SIZE, color='red')
yellow = align(11*Board.SQUARE_SIZE, 2*Board.SQUARE_SIZE, color='yellow')
blue = align(11*Board.SQUARE_SIZE, 11*Board.SQUARE_SIZE, color='blue')


root.mainloop()