import numpy as np
from tkinter import *
from pymongo import *
#from pprint import *
from bson.objectid import ObjectId
client = MongoClient('localhost',27017)

db = client.Bhuvnesh # CREATES DATABASE NAMED BHUVNESH
i=2
root =Tk()
var = StringVar()
var2 = StringVar()
label = Message( root, textvariable=var, relief=RAISED )
label2 = Message( root, textvariable=var2, relief=RAISED )
move_flag=0			#IF 0 'PIECE SELECT' ELSE 'MOVE POSITION SELECT'
color=['#8A360F',"white"]
MATCHCOUNT=0
Turn_Counter=0  	#'EVEN' for WHITE and 'ODD' for BLACK
startBoard = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"# w KQkq - 0 1"		FEN Code USED to create STARTING BOARD
matrix = [[0 for x in range(8)] for y in range(8)]

Pb = PhotoImage(file = 'BlackPawn.png', height = 80,width = 80) 
Rb = PhotoImage(file = 'BlackRook.png', height = 80,width = 80) 
Nb = PhotoImage(file = 'BlackKnight.png', height = 80,width = 80) 
Bb = PhotoImage(file = 'BlackBishop.png', height = 80,width = 80) 
Qb = PhotoImage(file = 'BlackQueen.png', height = 80,width = 80) 
Kb = PhotoImage(file = 'BlackKing.png', height = 80,width = 80) 
Pw = PhotoImage(file = 'WhitePawn.png', height = 80,width = 80) 
Rw = PhotoImage(file = 'WhiteRook.png', height = 80,width = 80) 
Nw = PhotoImage(file = 'WhiteKnight.png', height = 80,width = 80) 
Bw = PhotoImage(file = 'WhiteBishop.png', height = 80,width = 80) 
Qw = PhotoImage(file = 'WhiteQueen.png', height = 80,width = 80) 
Kw = PhotoImage(file = 'WhiteKing.png', height = 80,width = 80) 
transparen = PhotoImage(file = "transparency.png" , height = 80, width = 80)

d_img = { 'p' : Pb,		'r' : Rb,
		'n' : Nb,		'b' : Bb,
		'q' : Qb,		'k' : Kb,
		'P' : Pw,		'R' : Rw,
		'N' : Nw,		'B' : Bw,
		'Q' : Qw,		'K' : Kw}

d_mat = { 'p' : -1,		'r' : -6,
		'n' : -5,		'b' : -4,
		'q' : -3,		'k' : -2,
		'P' : 1,		'R' : 6,
		'N' : 5,		'B' : 4,
		'Q' : 3,		'K' : 2}

d_class = { 'p' : -1,		'r' : -6,
		'n' : -5,		'b' : -4,
		'q' : -3,		'k' : -2,
		'P' : 1,		'R' : 6,
		'N' : 5,		'B' : 4,
		'Q' : 3,		'K' : 2}
	
		
#ACCESS DATABSE 'MOVE' TO GET THE NUMBER OF MATCH 
def getDatabase():
	M1 = db.move.find()
	max=0
	for entry in M1:
		if entry['Count'] > max:
			max = entry['Count']
	global MATCHCOUNT
	
	MATCHCOUNT = max+1
	db.move.insert({'Count' : MATCHCOUNT})

#ACCESS THE DATABASE 'GAME' TO GET THE MOVE PLAYED BY BLACK
def getMatrixFromDB():
	M1 = db.game.find({'White' : matrix})	
	for entry in M1:
		mat = entry['Black']
		break
	#print (M1)
	return mat
	

#MATRIX TO BOARD
def matToBoard(matrix):
	White_box_image = PhotoImage(file = "L_brown.png",height =100,width=100)
	Black_box_image = PhotoImage(file = "D_brown.png",height =100,width=100)
	
	for row in range(0,8):
		for col in range(0,8):
			if matrix[row][col] == 0:
				Box_button[row][col].configure( image = transparen)
			else:
				p=matrix[row][col]
				for name, n in d_mat.items(): # for name, age in list.items():  (for Python 3.x)
					if n == p:
						piece= name
				img = d_img[piece]
				Box_button[row][col].configure(image = img)

#MAKE THE TURN		
def BlackTurn():
	global matrix
	matrix = getMatrixFromDB()
	matToBoard(matrix)
	
class Pawn(object):
	move_array=[]
	def get_valid_move(self,rows,cols):
		self.move_array=[]
		if(matrix[rows][cols]>0):
			if matrix[rows-1][cols] == 0:
				self.move_array.append([rows-1,cols])
			if matrix[rows-1][cols-1] < 0 :
				self.move_array.append([rows-1,cols-1])
			if cols < 7:
				if (matrix[rows-1][cols+1] < 0) :
					self.move_array.append([rows-1,cols+1])
			print (self.move_array)
			
			
		else :
			if matrix[rows+1][cols] == 0:
				self.move_array.append([rows+1,cols])
			if matrix[rows+1][cols-1] > 0:
				self.move_array.append([rows+1,cols-1])
			if cols < 7:
				if matrix[rows+1][cols+1] > 0 and (cols < 7):
					self.move_array.append([rows+1,cols+1])
			print (self.move_array)
		return self.move_array

class King(object): 
	move_array=[]
	def get_valid_move(self,row,col):
		self.move_array=[]
		if(matrix[row][col]>0):
			for i in range(0,3):
				for j in range(0,3): 
					if not(row-1+i == 8) or (col-1+j == 8) or (row-1+i == -1) or (col-1+j == -1)  :
						
						if matrix[row-1+i][col-1+j] == 0:
							self.move_array.append([row-1+i,col-1+j])
						if matrix[row-1+i][col-1+j] < 0 :
							self.move_array.append([row-1+i,col-1+j])			
			print (self.move_array)
			
		else :
			for i in range(0,3):
				for j in range(0,3): 
					if not((row-1+i == 8) or (col-1+j == 8) or (row-1+i == -1) or (col-1+j == -1)) :
					
						if matrix[row-1+i][col-1+j] == 0:
							self.move_array.append([row-1+i,col-1+j])
						if matrix[row-1+i][col-1+j] > 0 :
							self.move_array.append([row-1+i,col-1+j])			
			print (self.move_array)
		return self.move_array

	def getKingPos(self):
		for row in range(0,8):
			for col in range(0,8):
				if Turn_Counter %2 ==0:
					if matrix[row][col]== 2:
						return [row,col]
				else:
					if matrix[row][col]== -2:
						return row, col

	def InCheck(self,row_,col_):
		valid_move=[]
		valid_move_king=self.get_valid_move(row_,col_)
		count_flag=len(valid_move_king)
		
		if Turn_Counter%2 == 0:		
		
			#CHECKING POSSIBLE VALUES OF ALL BLACK PIECES
			for row in range(0,8):
				for col in range(0,8):
					
					#If Piece is a Pawn
					if(matrix[row][col]==-1 ):
						P=Pawn()
						print ("Pawn")
						valid_move+=P.get_valid_move(row,col)#Valid move Coordinates
						
						continue
					
					#If Piece is a King
					if(matrix[row][col]==-2 ):
						K=King()
						print ("King")
						valid_move+=K.get_valid_move(row,col)
						continue
					
					#If Piece is a Queen
					if(matrix[row][col]==-3 ):
						Q=Queen()
						print ("Queen")
						valid_move+=Q.get_valid_move(row,col)
						continue
					
					#If Piece is a Bishop
					if(matrix[row][col]==-4 ):
						B=Bishop()
						print ("Bishop")
						valid_move+=B.get_valid_move(row,col)
						continue
						
					
					#If Piece is a Knight
					if(matrix[row][col]==-5 ):
						N=Knight()
						print ("Knight")
						valid_move+=N.get_valid_move(row,col)
						continue
					
					#If Piece is a Rook
					if(matrix[row][col]==-6 ):
						R=Rook()
						print ("Rook")
						valid_move+=R.get_valid_move(row,col)
						continue
		else:
		
			#CHECKING POSSIBLE VALUES OF ALL WHITE PIECES
			for row in range(0,8):
				for col in range(0,8):
					
					#If Piece is a Pawn
					if(matrix[row][col]==1 ):
						P=Pawn()
						print ("Pawn")
						#move_flag=1
						valid_move+=P.get_valid_move(row,col)#Valid move Coordinates
						#valid_move.remove([row-1,col])
						continue
					
					#If Piece is a King
					if(matrix[row][col]==2 ):
						K=King()
						print ("King")
						valid_move+=K.get_valid_move(row,col)
						continue
					
					#If Piece is a Queen
					if(matrix[row][col]==3 ):
						Q=Queen()
						print ("Queen")
						valid_move+=Q.get_valid_move(row,col)
						continue
					
					#If Piece is a Bishop
					if(matrix[row][col]==4 ):
						B=Bishop()
						print ("Bishop")
						valid_move+=B.get_valid_move(row,col)
						continue
					
					#If Piece is a Knight
					if(matrix[row][col]==5 ):
						N=Knight()
						print ("Knight")
						valid_move+=N.get_valid_move(row,col)
						continue
					
					#If Piece is a Rook
					if(matrix[row][col]==6 ):
						R=Rook()
						print ("Rook")
						valid_move+=R.get_valid_move(row,col)
						continue
		
		#for tuple_i in range(0,len(valid_move_king)):
		#	if valid_move_king[tuple_i] in valid_move:
		#		del valid_move_king[tuple_i]
		if [row_,col_] in valid_move:
			print("SAFE NHI H")
			return 1
		else:
			print("SAFE KYUN H ")
			return 2
		
class Knight(object):
	move_array=[]
	def get_valid_move(self,row,col):
		self.move_array=[]
		#IF WHITE
		if matrix[row][col] > 0:
			i=2
			for j in range(-1,2,2):
				if row-i > -1:
					if col + j > -1 and col + j < 8:
						if matrix[row-i][col+j] <= 0:
							self.move_array.append([row-i,col+j])
				
				if row+i < 8:
					if col + j > -1 and col + j < 8:
						if matrix[row+i][col+j] <= 0:
							self.move_array.append([row+i,col+j])
				
				if col + i < 8:
					if row + j > -1 and row + j < 8:
						if matrix[row+j][col+i] <= 0:
							self.move_array.append([row+j,col+i])
				
				if col - i > -1:
					if row + j > -1 and row + j < 8:
						if matrix[row+j][col-i] <= 0:
							self.move_array.append([row+j,col-i])
				
				print (self.move_array)
		#IF BLACK
		else:
			i=2
			for j in range(-1,2,2):
				if row-i > -1:
					if col + j > -1 and col + j < 8:
						if matrix[row-i][col+j] >= 0:
							self.move_array.append([row-i,col+j])
				
				if row+i < 8:
					if col + j > -1 and col + j < 8:
						if matrix[row+i][col+j] >= 0:
							self.move_array.append([row+i,col+j])
				
				if col + i < 8:
					if row + j > -1 and row + j < 8:
						if matrix[row+j][col+i] >= 0:
							self.move_array.append([row+j,col+i])
				
				if col - i > -1:
					if row + j > -1 and row + j < 8:
						if matrix[row+j][col-i] >= 0:
							self.move_array.append([row+j,col-i])
				
				print (self.move_array)
		return  self.move_array
		
class Rook(object):
	move_array=[]
	def get_valid_move(self,row,col):
		self.move_array=[]
		if(matrix[row][col]>0):
			#UP
			for i in range(row-1,-1,-1):
				if (matrix[i][col]==0):
					self.move_array.append([i,col])
				if (matrix[i][col]<0):
					self.move_array.append([i,col])
					break
				if (matrix[i][col] > 0):
					#self.move_array.append([i,col])
					break
			#right		
			for i in range(col+1,8):
				if (matrix[row][i] == 0):
					self.move_array.append([row,i])
				if (matrix[row][i] < 0):
					self.move_array.append([row,i])
					break
				if (matrix[row][i] > 0):
					break
			
			#down
			for i in range(row+1, 8):
				if (matrix[i][col]==0):
					self.move_array.append([i,col])
				if (matrix[i][col]<0):
					self.move_array.append([i,col])
					break
				if (matrix[i][col] > 0):
					#self.move_array.append([i,col])
					break
			
			#left
			for i in range(col-1,-1,-1):
				if (matrix[row][i] == 0):
					self.move_array.append([row,i])
				if (matrix[row][i] < 0):
					self.move_array.append([row,i])
					break
				if (matrix[row][i] > 0):
					break
		else:
			#UP
			for i in range(row-1,-1,-1):
				if (matrix[i][col]==0):
					self.move_array.append([i,col])
				if (matrix[i][col]>0):
					self.move_array.append([i,col])
					break
				if (matrix[i][col] < 0):
					#self.move_array.append([i,col])
					break
			#right		
			for i in range(col+1,8):
				if (matrix[row][i] == 0):
					self.move_array.append([row,i])
				if (matrix[row][i] > 0):
					self.move_array.append([row,i])
					break
				if (matrix[row][i] < 0):
					break
			
			#down
			for i in range(row+1, 8):
				if (matrix[i][col]==0):
					self.move_array.append([i,col])
				if (matrix[i][col]>0):
					self.move_array.append([i,col])
					break
				if (matrix[i][col] < 0):
					#self.move_array.append([i,col])
					break
			
			#left
			for i in range(col-1,-1,-1):
				if (matrix[row][i] == 0):
					self.move_array.append([row,i])
				if (matrix[row][i] > 0):
					self.move_array.append([row,i])
					break
				if (matrix[row][i] < 0):
					break
		print (self.move_array)
		return  self.move_array

class Bishop(object):
	move_array=[]
	def get_valid_move(self,row,col):
		self.move_array=[]
		if(matrix[row][col]>0):
			
			#Left Diagonal UP and DOWN
			for i in range(1,col+1):
				if row-i < 0:
					break
				if(matrix[row-i][col-i] == 0):
					self.move_array.append([row-i,col-i])
				if(matrix[row-i][col-i] > 0):
					break
				if(matrix[row-i][col-i] < 0):
					self.move_array.append([row-i,col-i])
					break
				
			print (self.move_array)
			for i in range(1,col+1):
				if not (row+i >= 8)  :
					if matrix[row+i][col-i] == 0:
						self.move_array.append([row+i,col-i])
					if(matrix[row+i][col-i] > 0):
						break
					if(matrix[row+i][col-i] < 0):
						self.move_array.append([row+i,col-i])
						break
				
			print (self.move_array)
			#Right Diagonal 
			k=1
			for i in range(row - 1 ,-1,-1):
				if i < 0:
					break
				if not (col+k >= 8) :
					if(matrix[i][col+k]==0):
						self.move_array.append([i,col+k])
					if(matrix[i][col+k] > 0):
						break
					if(matrix[i][col+k]<0):
						self.move_array.append([i,col+k])
						break
				
				k=k+1
			print (self.move_array)
			#right down
			k=1
			for i in range(row+1,8):
				
				if not (col+k >= 8) :
					if(matrix[i][col+k]==0):
						self.move_array.append([i,col+k])
					if(matrix[i][col+k] > 0):
						break
					if(matrix[i][col+k] < 0 ):
						self.move_array.append([i,col+k])
						break
				else:
					break
				k=k+1
			print (self.move_array)
			
		else:
			#Left Diagonal UP and DOWN
			for i in range(1,col+1):
				if row-i < 0:
					break
				if(matrix[row-i][col-i] == 0):
					self.move_array.append([row-i,col-i])
				if(matrix[row-i][col-i] < 0):
					break
				if(matrix[row-i][col-i] > 0):
					self.move_array.append([row-i,col-i])
					break
				
			print (self.move_array)
			for i in range(1,col+1):
				if not (row+i >= 8)  :
					if matrix[row+i][col-i] == 0:
						self.move_array.append([row+i,col-i])
					if(matrix[row+i][col-i] < 0):
						break
					if(matrix[row+i][col-i] > 0):
						self.move_array.append([row+i,col-i])
						break
				
			print (self.move_array)
			#Right Diagonal 
			k=1
			for i in range(row - 1 ,-1,-1):
				if i < 0:
					break
				if not (col+k >= 8) :
					if(matrix[i][col+k]==0):
						self.move_array.append([i,col+k])
					if(matrix[i][col+k] < 0):
						break
					if(matrix[i][col+k]>0):
						self.move_array.append([i,col+k])
						break
				
				k=k+1
			print (self.move_array)
			#right down
			k=1
			for i in range(row+1,8):
				if not (col+k >= 8) :
					if(matrix[i][col+k]==0):
						self.move_array.append([i,col+k])
					if(matrix[i][col+k] < 0):
						break
					if(matrix[i][col+k] > 0 ):
						self.move_array.append([i,col+k])
						break
				else:
					break
				k=k+1
			print (self.move_array)
		return  self.move_array

class Queen(object):
	move_array=[]
	move_array2=[]
	def get_valid_move(self,row,col):
		B=Bishop()
		self.move_array=B.get_valid_move(row,col)
		R=Rook()
		self.move_array2=R.get_valid_move(row,col)
		print(self.move_array2)
		self.move_array2=self.move_array2+self.move_array
		print(self.move_array2)
		return self.move_array2

def pieceMove(initial_row,initial_col,new_row,new_col,p):
	global matrix
	White_box_image = PhotoImage(file = "L_brown.png",height =100,width=100)
	Black_box_image = PhotoImage(file = "D_brown.png",height =100,width=100)
	
	for name, n in d_mat.items(): 
		if n == p:
			piece= name
	
	#piece_img = dict.get(p)
	img=d_img[piece]
	Box_button[new_row][new_col].configure(image = img)
	Box_button[initial_row][initial_col].configure(image = Black_box_image)
	'''
	if (rows+cols) %2 ==0:
		Box_button[rows][cols].configure(image= White_box_image)
	else:	
		Box_button[rows][cols].configure(image = transparen)
	'''
	Box_button[initial_row][initial_col].configure( image = transparen)
		
	matrix[new_row][new_col]=matrix[initial_row][initial_col]
	matrix[initial_row][initial_col]=0

def piecePlace(row,col,p):
	global matrix
	White_box_image = PhotoImage(file = "L_brown.png",height =100,width=100)
	Black_box_image = PhotoImage(file = "D_brown.png",height =100,width=100)
	
	for name, n in d_mat.items(): 
		if n == p:
			piece= name
	img=d_img[piece]
	Box_button[row][col].configure(image = img)
	matrix[row][col]= p

	
def leftClick(rows,cols):
	print(rows,cols)
	global initial_col,initial_row,valid_row, valid_col
	global move_flag,Turn_Counter
	global valid_move,prev_matrix
	global label,label2
	global var,var2
	if move_flag == 0:
		if (((Turn_Counter %2 == 0) and (matrix[rows][cols] >0)) or ((Turn_Counter %2 != 0 ) and (matrix[rows][cols]<0))):
		#if move_flag == 0:#if 0 piece select else move position select
			
			initial_row=rows
			initial_col=cols
			
			#If Piece is a Pawn
			if(matrix[rows][cols]==-1 or matrix[rows][cols]==1):
				P=Pawn()
				valid_move=P.get_valid_move(rows,cols)#Valid move Coordinates
				#move_flag=1
		
			#If Piece is a King
			if(matrix[rows][cols]==-2 or matrix[rows][cols]==2):
				K=King()
				valid_move=K.get_valid_move(rows,cols)
				
			#If Piece is a Queen
			if(matrix[rows][cols]==-3 or matrix[rows][cols]==3):
				Q=Queen()
				valid_move=Q.get_valid_move(rows,cols)
				
			#If Piece is a Bishop
			if(matrix[rows][cols]==-4 or matrix[rows][cols]==4):
				B=Bishop()
				valid_move=B.get_valid_move(rows,cols)
				
			#If Piece is a Knight
			if(matrix[rows][cols]==-5 or matrix[rows][cols]==5):
				N=Knight()
				valid_move=N.get_valid_move(rows,cols)
				
			#If Piece is a Rook
			if(matrix[rows][cols]==-6 or matrix[rows][cols]==6):
				R=Rook()
				valid_move=R.get_valid_move(rows,cols)	
					
			if len(valid_move) > 0:
				move_flag=1
			else:
				move_flag=0
		
		else:
			print("INVALID MOVE")
			
	else:
		if len(valid_move) > 0:	
			if [rows,cols] in valid_move:
				temp= matrix[rows][cols]
				pieceMove(initial_row,initial_col,rows,cols,matrix[initial_row][initial_col])#valid_row,valid_col,matrix[initial_row][initial_col])
				K2=King()
				row_ , col_ = K2.getKingPos()
				print ("KING KI POSITION")
				print (row_,col_)
				valid_move2 = K2.InCheck(row_,col_)
				
				if valid_move2 == 2:
					valid_move = []
					print (matrix)
					x = int(Turn_Counter/2) + 1
					if Mode == 1:
						
						if Turn_Counter % 2 ==0:
							#s = str(matrix)
							db.game.insert({'MATCHCOUNT' : MATCHCOUNT, 'Turn' : x,  'White' :matrix})
						else:
							#s = str(matrix)
							db.game.update({'MATCHCOUNT' : MATCHCOUNT, 'Turn' : x},{"$set": {"Black": matrix}})
						
					else:#if Mode == 2:
						Turn_Counter = Turn_Counter+1
						BlackTurn()
					
					move_flag = 0
					Turn_Counter = Turn_Counter+1
					print("safe hai")
					
				elif valid_move2 == 1:
					valid_move=[]
					move_flag = 0
					print("SAFE NHI H")
					#    initial (from), new position (to)     , image at initial
					pieceMove(rows,cols,initial_row,initial_col,matrix[rows][cols])
					piecePlace(rows,cols,temp)	# PLACE OLD PIECE
					print("Wrong Move")
			else:
				valid_move=[]
				print("Wrong Move")
				move_flag = 0
	if(Turn_Counter %2 ==0):
		var.set("WHITE TURN")
	else:
		var.set("BLACK TURN")
	
	label.pack()


def pieces():
	boxCounter=0;
	global matrix,prev_matrix	
	rows=0
	cols=0
	for i in range(0,len(startBoard)):
		print (rows,cols)
		if startBoard[boxCounter].isalpha() :
			img=d_img[startBoard[boxCounter]]
			matrix[rows][cols]=d_mat[startBoard[boxCounter]]
			Box_button[rows][cols].configure(image = img, height = 80,width = 80)
			cols=cols+1
			boxCounter=boxCounter+1
	
		elif startBoard[boxCounter]== '/':
			boxCounter=boxCounter+1
			cols=0
			rows=rows+1
			
		elif startBoard[boxCounter].isnumeric():
			num = int(startBoard[boxCounter])
			cols = cols + num
			boxCounter=boxCounter+1
		elif cols>7:
			cols=0
			rows=rows+1
			boxCounter=boxCounter+1
		elif rows>7:
			break;
	print(matrix)
	for rows in range(0,8):
		for cols in range(0,8):
			if matrix[rows][cols]==0 :
				Box_button[rows][cols].configure( image = transparen)
	prev_matrix=[]
	
def ModeDeclare(M):
	global Mode
	Mode=M
	print(Mode)
	pieces()
	#Mode_button.configure(state = DISABLED)
	#Mode_button2.configure(state = DISABLED)

def boardButtons(root):
	board = Frame(root,height = 100,width = 100)
	global Box_button, Mode 
	Box_button = [[
	0 for x in range(0,8)] for x in range(0,8)]
	White_box_image = PhotoImage(file = "L_brown.png",height =100,width=100)
	Black_box_image = PhotoImage(file = "D_brown.png",height =100,width=100)
	board.grid(row=0,column=0)
	for rows in range(0,8):
		for cols in range(0,8):
			handler = lambda r = rows,c= cols : leftClick(r,c)	
			if (rows+cols) %2 ==0:				
				Box_button[rows][cols] = Button(board,bg=color[1],image= White_box_image,height= 80,width=80, command = handler)
				#whiteBox_button[rows][cols].grid(row = rows,column = cols )		
			else:	
				Box_button[rows][cols] = Button(board,bg=color[0] ,image = Black_box_image, height= 80,width=80, command= handler)
			Box_button[rows][cols].grid(row = rows,column = cols )
	board.pack(side="left",fill="y")

	var.set("SELECT A GAMEPLAY MODE")
	label.pack()
	handler1 = lambda Mode = 1 : ModeDeclare(Mode)
	handler2 = lambda Mode = 2 : ModeDeclare(Mode)
	Mode_button = Button(root,height= 5,width=10,text = 'P vs P',command = handler1  )
	Mode_button2 = Button(root,height= 5,width=10,text = 'P vs AI', command = handler2 )
	Mode_button2.pack(side = RIGHT)
	Mode_button.pack(side = RIGHT)
	
#getDatabase()
root.title("GAME of CHESS")
boardButtons(root)
root.mainloop()		
