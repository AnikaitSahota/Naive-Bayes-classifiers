"""
Author : Anikait Sahota
Status : no error
Dated : 21 March 2019


"""

def matrix_multiplication(a,b):
	""" function to multiply matrix a with matrix b -> aXb 
	Arguments:
		a and b are two dimensional matrices """
	if len(a[0])!=len(b):		# if number of columns of matrix a == number of rows of matrix b
		return(False)  			# these matrices can't be multiplied hence False
	tmp_k=len(b)
	m_a=len(a)		#number of rows
	n_b=len(b[0])	#number of columns
	result=[[None for i in range (n_b)] for i in range (m_a)]		#creating matrix with dimensions of resultanst matrix
	for i in range (m_a):
		for j in range (n_b):
			sum=0
			for k in range (tmp_k):
				sum+=a[i][k]*b[k][j]
			result[i][j]=float(sum)
	return(result)
def transpose(a):
	""" function to return transpose of 'a' matrix
	Arguments:
		a  is the input matrix """
	m = len(a)			# numner of rows in given matrix
	n = len(a[0])		# number of columns in given matrix
	result = [[None for i in range (m)] for j in range (n)]		#creating a matrix while swaping the number of rows with number of columns
	for i in range(m) :		# for loop to assign values to result matrix
		for j in range(n):
			result[j][i] = a[i][j]
	return(result)		# returning the matrix
def determinent(a):
	""" function to return determinent of the given matrix a using the recursiion 
	Argument: 
		a is the input square matrix to find determinent"""
	n = len(a)
	if(n == 1):			# base case for 1X1 square matric
		return a[0][0] ;
	elif(n == 2):		# base case for 2X2 square matrix
		return(a[0][0]*a[1][1] - a[0][1]*a[1][0])
	else:				# for all cases above 2X2
		result = 0		# resultant determinent
		tmp_matrix = [[None for i in range (n-1)]for j in range (n-1)]	# matrix with (n-1)X(n-1) dimensions for recursion
		for i in range (n):
			for j in range (n):		# loop for assigning the value to (n-1)X(n-1) square matrix
				temp_index = 0
				for k in range (n):
					if(k != i and temp_index < n and j>0):
						tmp_matrix[j-1][temp_index] = a[j][k]
						temp_index += 1
			result += ((-1)**(i))*(a[0][i])*determinent(tmp_matrix)		# calculating the determinent
		return result 	# returning the determinent value
def Adjoint(a):
	""" fuction to find adjoint of a matrix and return it
	Argument:
		a is the input matrix"""
	n = len(a)			# number of columns and rows of square matrix
	result = [[None for i in range (n)]for j in range(n)]
	if(n == 1):		# base case for 1X1 matrix
		result[0][0] = 1
	elif(n == 2):	# base case for 2X2 matrix
		result[0][0] = a[1][1]
		result[0][1] = -1*a[0][1]
		result[1][0] = -1*a[1][0]
		result[1][1] = a[0][0]
		""" it converts matrix 
			| a  b |   -->   | d  -b |
			| c  d |         | -c  a |        """
	else:
		tmp_matrix = [[None for i in range (n-1)]for j in range (n-1)]		# tempararory matrix for finding determinent
		for i in range (n):		# for loop for result matrix
			for j in range (n):		# for loop for result matrix
				tmp_i = 0
				for k in range (n):		# for loop for formig determinent matrix
					tmp_j = 0
					for l in range (n):		# for loop for forming determinent matrix
						if(k != i and l != j):
							tmp_matrix[tmp_i][tmp_j] = a[k][l]
							tmp_j += 1
							if(tmp_j == n-1):
								tmp_i += 1
				result[j][i] = ((-1)**(i+j))*determinent(tmp_matrix)	# used (j,i) instead of (i,j) to form transpose
	return result 		# returning the Adjoint matrix of a
def inverse(a) :
	""" function to find inverse of a matrix
		return inverse of matrix if possible othervise Fasle
	Arguments:
		a is the input matrix """
	det = determinent(a)		# finding determinent of matrix 'a'
	if(det == 0):			# if det == 0 hence it is singular matrix , inverse not possible
		return False
	Adj = Adjoint(a)		# finding Adjoint of matrix
	if(det != 1):
		for i in range (len(a)):		# for loop Adj(a)/det(a)
			for j in range (len(a)):
				Adj[i][j] /= det
	return Adj  		# returning the inverse of matrix 'a'

a = [['Ab','Cd'],['Ef','Gh']]
#print(transpose(a))