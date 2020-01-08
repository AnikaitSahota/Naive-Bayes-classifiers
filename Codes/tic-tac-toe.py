filepath = 'DataSheets/Tic-Tac-Toe/tic-tac-toe.data'
X = []
Y = []
DataRow = []
import Probability
import Matrix

with open(filepath,'r') as f :
	for line in f :
		DataRow.append(list(line.split(',')))		# maintaining list of rows
		X.append([DataRow[-1][0]])
		for i in range (1,9):
			X[-1].append(DataRow[-1][i])	# maintaining 2D matrix for Xs
#			X[-1].append(i)
		Y.append([DataRow[-1][-1][:-1]])		# maintaining 2D matrix for Ys

numer = 0

for i in range (len(X)):
	train_X = X[:]
	X_test = train_X[i]
	train_X.remove(train_X[i])
	train_Y = Y[:]				# making a temporary matrix
	Y_test = train_Y[i][0]		# storing values of test set
	train_Y.remove(train_Y[i])	# making traning set
	SetX , SetY , All_Cond_Probs = Probability.All_Cond_Prob(train_X,train_Y)
	ProbY = Probability.ProbY(SetY,train_Y)
	Pridicted = Probability.classification(SetY,SetX,ProbY,All_Cond_Probs,[X_test],[Y_test])
	if(Y_test == Pridicted[0]):
		numer += 1

Accuracy = numer/len(X)
print('tic-tac-toe Endgame',Accuracy)

with open('final_data.csv','w') as file:
	file.write('DataSheet Name,Accuracy rate\n')
	file.write('tic-tac-toe Endgame,'+str(Accuracy)+'\n')
