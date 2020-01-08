# Author : Anikait Sahota
import Probability

filepath1_test = 'DataSheets/Spect Heart/SPECT.test'
filepath1_train = 'DataSheets/Spect Heart/SPECT.train'
DataRow = []
X =[]
Y = []

with open(filepath1_train,'r') as f :
	for line in f :
		DataRow.append(list(map(int,line.split(','))))		# maintaining list of rows
		X.append([DataRow[-1][1],])
		for i in range (2,23):
			X[-1].append(DataRow[-1][i])	# maintaining 2D matrix for Xs
#			X[-1].append(i)
		Y.append([DataRow[-1][0]])		# maintaining 2D matrix for Ys
#		print(Y[-1])
#print(len(X[-1]))
SetX ,SetY , All_Cond_Probs = Probability.All_Cond_Prob(X,Y)
ProbY = Probability.ProbY(SetY,Y)
DataRow = []
X =[]
Y = []
numer = 0 ;

with open(filepath1_test,'r') as f :
	for line in f :
		DataRow.append(list(map(int,line.split(','))))
		Y.append([DataRow[-1][0]])
		X.append([DataRow[-1][1]])
		for i in range (2,23):
			X[-1].append(DataRow[-1][i])	# maintaining 2D matrix for Xs
		YPredict = Probability.classification(SetY,SetX,ProbY,All_Cond_Probs,[X[-1]],[Y[-1]])
#		print(X[0])
		if(Y[-1][0] == YPredict[0]):
			numer += 1

Accuracy = numer/len(X)
print('Spect Heart',Accuracy)

with open('final_data.csv','a') as file:
	file.write('Spect Heart,'+str(Accuracy)+'\n')
