
def findempty(grid,row,col):
	#row=0
	col=0
	for row in range(row,9):
		for col in range(9):
			if grid[row][col]==0:
				return row,col,True
	return row,col,False 

	
#CHECK THE 3*3 SMALL GRID	
def checkSmallBox(grid,row,col,num):
	j=col-(col%3)
	i=row-(row%3)
	x=i
	y=j
	for x in range(i,i+3):
		for y in range(j,j+3):
			if grid[x][y]== num:
				return False
	return True

	
#CHECK HORIZONTAL AND VERTICAL
def checkXY(grid,row,col,num):
	#HORIZONTAL
	for x in range(9):
		if grid[row][x]== num:
			return False
	#VERTICAL
	for x in range(9):
		if grid[x][col]== num:
			return False
	return True
	
	
	
def Sudoku(grid,row,col):
	arr=[1,2,3,4,5,6,7,8,9]
	k=0
	
	#CHECK WHETHER THERE IS ANY BLANK BOX
	row,col,result=findempty(grid,row,col)
	if result==False :
		return True
		
		
	for k in range(1,10):
		if checkSmallBox(grid,row,col,k):
			if checkXY(grid,row,col,k):
				grid[row][col]=k
				if Sudoku(grid,row,col):
					return True
				grid[row][col]=0
	return False 
	
	
def main():
	grid=[[0,8,3,0,0,1,6,0,0],
		[0,7,0,4,0,0,0,2,1],
		[5,0,0,3,9,6,0,0,0],
		[2,0,4,0,5,0,1,3,0],
		[0,0,8,9,0,7,5,0,0],
		[0,5,7,0,3,4,9,0,2],
		[0,0,0,5,6,3,0,0,9],
		[3,1,0,0,0,2,0,5,0],
		[0,0,5,8,0,0,0,4,0]]
	#print (grid)
	#print("ENTER THE SUDOKU")
	#for i in range(0,9):
	#		for j in range(0,9):
	#			grid[i][j]=input();
	i=0
	j=0
	for i in range(0,9):
		print (grid[i])

	if Sudoku(grid,0,0):
		print("SOLUTION")
		for i in range(0,9):
			print (grid[i])
			
	else:
		print ("NO SOLUTION EXISTS")
	
if __name__=='__main__':
	main()