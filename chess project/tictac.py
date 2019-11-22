from tkinter import *
from PIL import Image, ImageFont, ImageDraw, ImageTk
import pygame
import numpy as np
def check():
	global matrix
	row_sum = matrix.sum(axis = 1)
	col_sum = matrix.sum(axis = 0)
	main_dia_sum = matrix.trace()
	off_dia_sum = matrix[0][2]+matrix[1][1]+matrix[2][0]
	for i in range(0,3):
		if (row_sum[i] == -3) or (row_sum[i] == 3):
			for col in range(0,3):
				Box_button[i][col].configure(bg = "red",state = DISABLED)
			for row in range(0,3):
				for col in range(0,3):
					Box_button[row][col].configure(state = DISABLED)
			break	

		if (col_sum[i] == -3) or (col_sum[i] == 3):
			for row in range(0,3):
				Box_button[row][i].configure(bg = "red",state = DISABLED)
			for row in range(0,3):
				for col in range(0,3):
					Box_button[row][col].configure(state = DISABLED)
			break
			
		if (main_dia_sum == -3) or (main_dia_sum == 3):
			for row in range(0,3):
				Box_button[row][row].configure(bg = "red",state = DISABLED)
			
			for row in range(0,3):
				for col in range(0,3):
					Box_button[row][col].configure(state = DISABLED)
			break
			
		if (off_dia_sum == -3) or (off_dia_sum == 3):
			for row in range(0,3):
				Box_button[row][2-row].configure(bg = "red",state = DISABLED)
			
			for row in range(0,3):
				for col in range(0,3):
					Box_button[row][col].configure(state = DISABLED)
			break		
def leftClick( r , c ,circle_image,cross_image):

	global matrix,player_chance,circle_count,cross_count
	x=player_chance
	
	# TRIGGERS circle WHEN player_chance = 2 & cross WHEN player_chance = 1
 	# -1 in matrix for circle
	# 1 in matrix for cross
	if x == 2 : 
		Box_button[r][c].configure(image = circle_image, state = DISABLED)#bg = "circle" ,state = DISABLED)
		player_chance = 1
		matrix[r][c] = -1
		circle_count += 1
		if circle_count >= 3:
			check()
	else:
		Box_button[r][c].configure(image = cross_image, state = DISABLED)#(bg = "cross" ,state= DISABLED)
		player_chance = 2
		matrix[r][c] = 1
		cross_count += 1
		if cross_count >= 3:
			check()
		
	Box_button[r][c].grid(row = r,column = c )

	
def main():
	global matrix
	matrix = np.zeros((3,3), dtype = np.int) #[[ 0 for x in range(0,3)] for x in range(0,3)]
	global circle_count 
	circle_count = 0
	global cross_count
	cross_count=0
	global player_chance
	player_chance =1
	global Box_button
	Box_button= [[ 0 for x in range(0,3)] for x in range(0,3)]
	circle_image = PhotoImage(file = "circle3.png",height =100,width=100)
	cross_image = PhotoImage(file = "cross2.png",height =100,width=100)
	White_box_image = PhotoImage(file = "White_square.png",height =100,width=100)
	board=Frame(root,height=300,width=300)
	board.grid(row=0,column=0)
	for rows in range(0,3):
		for cols in range(0,3):
			handler = lambda r=rows,c=cols: leftClick(r,c,circle_image,cross_image)#Box_button[r][c].cnfigure(bg = "cross",state= DISABLED)
			Box_button[rows][cols] = Button(board,image=White_box_image,command= handler)
			Box_button[rows][cols].grid(row = rows,column = cols )
			
	handler2 = lambda : main()
	Reset_button = Button(root, text= "RESET",command = handler2)
	Reset_button.grid(row = 3, columnspan = 3)
	root.mainloop()

root= Tk()
main()