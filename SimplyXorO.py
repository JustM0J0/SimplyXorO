#This is an X and O's game
from turtle import *
from tkinter import messagebox

#some obvious variables

_current_player = 'X' #Player X or O

tl,tc,tr = None, None , None

cl,cc,cr = None , None, None

bl,bc,br = None, None , None

def draw_line(x1,y1,x2,y2):
	hideturtle()
	penup()
	setposition(x1,y1)
	pendown()
	setposition(x2,y2)
	update()
	
def draw_board():
	draw_line(300,500, 300,200)
	draw_line(400,500,400,200)
	draw_line(200, 400, 500, 400)
	draw_line(200, 300, 500, 300)
	
def draw_X(x,y):
	draw_line(x-40,y+40, x+40,y-40)
	draw_line(x+40,y+40,x-40,y-40)

def draw_O(x,y):
	hideturtle()
	penup()
	setposition(x,y-40)
	pendown()
	circle(40)
	update()
	
def hit(x,y):
	box = None
	
	if 200<x<300 and 400<y<500:
		box = 'TopLeft'
	elif 300<x<400 and 400<y<500:
		box = 'TopCenter'
	elif 400<x<500 and 400<y<500:
		box = 'TopRight'
	elif 200<x<300 and 300<y<400:
		box = 'CenterLeft'
	elif 300<x<400 and 300<y<400:
		box = 'CenterCenter'
	elif 400<x<500 and 300<y<400:
		box = 'CenterRight'
	elif 200<x<300 and 200<y<300:
		box = 'BottomLeft'
	elif 300<x<400 and 200<y<300:
		box = 'BottomCenter'
	elif 400<x<500 and 200<y<300:
		box = 'BottomRight'
	return box
	
def center_box(box):
	if box == 'TopLeft':
		return 250, 450
	elif box == 'TopCenter':
		return 350, 450
	elif box == 'TopRight':
		return 450, 450
	elif box == 'CenterLeft':
		return 250, 350 
	elif box == 'CenterCenter':
		return 350, 350
	elif box == 'CenterRight':
		return 450, 350
	elif box == 'BottomLeft':
		return 250, 250
	elif box == 'BottomCenter':
		return 350, 250
	elif box == 'BottomRight':
		return 450, 250

def restart():
	clearscreen()
	draw_board()
	
	
def winner():
	if (tl==tr==tc=='X') or (tl==cl==bl=='X') or (cl==cr==cc=='X') or (bl==bc==br=='X') or (tc==bc==cc=='X') or (tr==br==cr=='X') or (tr==cc==bl=='X') or (tl==cc==br=='X'):
		messagebox.showinfo('Game Over', 'X wins')
		exitonclick()
	elif (tl==tr==tc=='O') or (tl==cl==bl=='O') or (cl==cr==cc=='O') or (bl==bc==br=='O') or (tc==bc==cc=='O') or (tr==br==cr=='O') or (tr==cc==bl=='O') or (tl==cc==br=='O'):
		messagebox.showinfo('Game Over', 'O wins')
		exitonclick()

def mouse_click(x,y):
	global tl,tc,tr,cl,cc,cr,bl,bc,br
	box = hit(x,y)
	x , y = center_box(box)
	if _current_player == 'X':
		if box == 'TopLeft' and tl != 'O':
			tl = 'X'
			draw_X(x,y)
			current_player()
		elif box == 'TopCenter' and tc!= 'O':
			tc = 'X'
			draw_X(x,y)
			current_player()
		elif box == 'TopRight' and tr != 'O':
			tr = 'X'
			draw_X(x,y)
			current_player()
		elif box == 'CenterLeft' and cl!= 'O':
			cl = 'X'
			draw_X(x,y)
			current_player()
		elif box == 'CenterCenter' and cc!= 'O':
			cc = 'X'
			draw_X(x,y)
			current_player()
		elif box == 'CenterRight' and cr!= 'O':
			cr = 'X'
			draw_X(x,y)
			current_player()
		elif box == 'BottomLeft' and bl!= 'O':
			bl = 'X'
			draw_X(x,y)
			current_player()
		elif box == 'BottomCenter' and bc!= 'O':
			bc = 'X'
			draw_X(x,y)
			current_player()
		elif box == 'BottomRight' and br!= 'O':
			br = 'X'
			draw_X(x,y)
			current_player()
		title('X and O\'s   Current Player is: ' + _current_player)
	elif _current_player == 'O':
		if box == 'TopLeft' and tl != 'X':
			tl = 'O'
			draw_O(x,y)
			current_player()
		elif box == 'TopCenter' and tc != 'X':
			tc = 'O'
			draw_O(x,y)
			current_player()
		elif box == 'TopRight' and tr != 'X': 
			tr = 'O'
			draw_O(x,y)
			current_player()
		elif box == 'CenterLeft' and cl!= 'X':
			cl = 'O'
			draw_O(x,y)
			current_player()
		elif box == 'CenterCenter' and cc!= 'X':
			cc = 'O'
			draw_O(x,y)
			current_player()
		elif box == 'CenterRight' and cr!= 'X':
			cr = 'O'
			draw_O(x,y)
			current_player()
		elif box == 'BottomLeft' and bl!= 'X':
			bl = 'O'
			draw_O(x,y)
			current_player()
		elif box == 'BottomCenter' and bc!= 'X':
			bc = 'O'
			draw_O(x,y)
			current_player()
		elif box == 'BottomRight' and br!= 'X':
			br = 'O'
			draw_O(x,y)
			current_player()
		title('X and O\'s   Current Player is: ' + _current_player)
	winner()

def current_player():
	global _current_player
	
	if _current_player == 'X':
		_current_player = 'O'
	else:
		_current_player = 'X'

def main():
	title('X and O\'s   Current Player is: ' + _current_player)
	tracer(0)
	bgcolor('orange')
	pensize(30)
	pencolor('blue')
	screensize(600,600)	
	setworldcoordinates(0,0,599,599)
	draw_board()
	onscreenclick(mouse_click)
	mainloop()
	
main()
