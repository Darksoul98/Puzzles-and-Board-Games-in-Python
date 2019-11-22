# Tic Tac Toe AI

import numpy as np
def findEmpty(mat,row=0,col=0):
	for row in range(0,3):
		for col in range(0,3):
			if mat[row][col] == 0 :
				return row,col,True
	return row,col,False
	
	
def checkSum(matrix,sum):
	row_sum = matrix.sum(axis = 1)
	col_sum = matrix.sum(axis = 0)
	main_dia_sum = matrix.trace()
	off_dia_sum = matrix[0][2]+matrix[1][1]+matrix[2][0]
	if (row_sum==sum)||(col_sum==sum)||(main_dia_sum==sum)||(off_dia_sum==sum):
		return True	
	else:
		return False
	
def ticTacToeAI(mat,row,col):
	arr=[-1,1]
	row,col,result = findEmpty(mat,row,col)
	if result==False:
		if checkSum
	alt=1
	for k in arr:		
		if checkSum(mat):
			return True
		else:
			if alt == 1:
				mat[row][col] = 1
				alt=2
			else:
				mat[row][col] = -1
				alt=1

			
def main():
	matrix = np.zeros((3,3), dtype = np.int)
	
if __name__=='__main__':
	main()
