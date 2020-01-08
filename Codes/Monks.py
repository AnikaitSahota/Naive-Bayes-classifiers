import Probability

filepath1_train = 'DataSheets/Monks Problems/monks-1.train'
filepath1_test = 'DataSheets/Monks Problems/monks-1.test'
filepath2_train = 'DataSheets/Monks Problems/monks-2.train'
filepath2_test = 'DataSheets/Monks Problems/monks-2.test'
filepath3_train = 'DataSheets/Monks Problems/monks-3.train'
filepath3_test = 'DataSheets/Monks Problems/monks-3.test'



def read_file(file_name):
	DataRow = []
	X = []
	Y = []
	with open(file_name,'r') as f :
		for line in f :
			DataRow.append(list(line.split(' ')))		# maintaining list of rows
			X.append([int(DataRow[-1][2])])
			for i in range (3,8):
				X[-1].append(int(DataRow[-1][i]))	# maintaining 2D matrix for Xs
			Y.append([int(DataRow[-1][1])])		# maintaining 2D matrix for Ys
	return(X,Y)



X , Y = read_file(filepath1_train)

SetX ,SetY , All_Cond_Probs = Probability.All_Cond_Prob(X,Y)
ProbY = Probability.ProbY(SetY,Y)
numer = 0

X , Y = read_file(filepath1_test)

for i in range(len(X)):
	YPredict = Probability.classification(SetY,SetX,ProbY,All_Cond_Probs,[X[i]],[Y[i]])
	if(Y[i][0] == YPredict[0]):
		numer += 1
accuracy1 = numer/len(X)
print('Monks-1',accuracy1)

#---------------------------------------------------------------------------------

X , Y = read_file(filepath2_train)

SetX ,SetY , All_Cond_Probs = Probability.All_Cond_Prob(X,Y)
ProbY = Probability.ProbY(SetY,Y)
numer = 0

X , Y = read_file(filepath2_test)

for i in range(len(X)):
	YPredict = Probability.classification(SetY,SetX,ProbY,All_Cond_Probs,[X[i]],[Y[i]])
	if(Y[i][0] == YPredict[0]):
		numer += 1
accuracy2 = numer/len(X)
print('Monks-1',accuracy2)

#-----------------------------------------------------------------------------------

X , Y = read_file(filepath3_train)

SetX ,SetY , All_Cond_Probs = Probability.All_Cond_Prob(X,Y)
ProbY = Probability.ProbY(SetY,Y)
numer = 0

X , Y = read_file(filepath3_test)

for i in range(len(X)):
	YPredict = Probability.classification(SetY,SetX,ProbY,All_Cond_Probs,[X[i]],[Y[i]])
	if(Y[i][0] == YPredict[0]):
		numer += 1
accuracy3 = numer/len(X)
print('Monks-1',accuracy3)

with open('final_data.csv','a') as file:
	file.write('Monks-1,'+str(accuracy1)+'\n')
	file.write('Monks-2,'+str(accuracy2)+'\n')
	file.write('Monks-3,'+str(accuracy3)+'\n')
