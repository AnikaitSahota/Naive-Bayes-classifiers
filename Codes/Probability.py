"""
Author : Anikait Sahota
"""
import Matrix

def Conditional_Probaility(X,Setx,Y,Sety):
	""" Function to calculate conditional probability for a feature --> P(xi | Cj )
	Arguments :
		X and Y  are Vectors containing a Xi and Y values (i.e. a feature) 
		and Setx and Sety are Vector containing unique values of X and Y"""
	Resultant_Matrix = [[0 for i in range (len(Sety))]for j in range (len(Setx))]
	Prob = [0 for i in range (len(Sety))]
	for i in range (len(X)):
		temp_i = Setx.index(X[i])
		temp_j = Sety.index(Y[i])
		Resultant_Matrix[temp_i][temp_j] += 1
		Prob[temp_j] += 1
	for i in range (len(Setx)):
		for j in range (len(Sety)):
			Resultant_Matrix[i][j] /= Prob[j]
#	print(Prob,Sety,Setx)
#	print(Resultant_Matrix)
	return(Resultant_Matrix)


def All_Cond_Prob(X,Y):
	XT = Matrix.transpose(X)
	YT = Matrix.transpose(Y)
	SetX = []
	SetY = []
	Cond_Probs = []
	for i in range (len(YT)):
		SetY.append(list(set(YT[i])))
	for i in range (len(XT)):
		SetX.append(list(set(XT[i])))
	for i in range(len(YT)):
		for j in range (len(XT)):
			Cond_Probs.append(Conditional_Probaility(XT[j],SetX[j],YT[i],SetY[i]))
#	print(SetY)
	return(SetX,SetY,Cond_Probs)

def ProbY(SetY,Y) :
	ResultProb = [[0 for i in range (len(SetY[j]))] for j in range (len(SetY))]
	temp_sum = [[0] for i in range (len(SetY))]
	YT = Matrix.transpose(Y)
	for i in range(len(YT)) :
		for j in range (len(YT[i])) :
			ResultProb[i][SetY[i].index(YT[i][j])] += 1
			temp_sum[i][0] += 1
	for i in range (len(SetY)):
		for j in range (len(SetY[i])) :
			ResultProb[i][j] /= temp_sum[i][0]
	return(ResultProb)
def classification(SetY,SetX,ProbY,All_Cond_Probs,X,Y):
	predicted_Y = []
	Prob = [[ProbY[j][i] for i in range (len(SetY[j]))] for j in range (len(SetY))]
	for t in range (len(SetY)):
		for i in range(len(SetY[t])) :
			for j in range (len(SetX)) :
#				print(i,j,'-------------')
#				print(SetX[j].index(X[0][j]),SetY[0])
				try :
					Prob[t][i] *= All_Cond_Probs[j][SetX[j].index(X[0][j])][i]
				except :
					Prob[t][i] = 0
		predicted_Y.append(SetY[t][Prob[t].index(max(Prob[t]))])
#	print(predicted_Y,Y)
#	print(Prob)
	return(predicted_Y)
