#!/usr/bin/python
from sklearn import svm
from sklearn import cross_validation
import numpy as np
def process_category(category,data):
    svc=svm.SVC(C=10)
    X=[]
    Y=[]
    for unit in data:
        vec=data[unit]['vector']
        X.append(vec)
        if data[unit]['actual']!=category:
            Y.append(-1)
        else:
            Y.append(1)

    dataX=np.array(X)
    dataY=np.array(Y)
    svc=svm.SVC(C=10)
    svc.fit(dataX,dataY)
    score=cross_validation.cross_val_score(svc,dataX,dataY,cv=10)
    return score

#-----script entry
games={}
#read raw data
header=True
for line in file('feedData.txt'):
    #skip header
    if header:
        header=False
        continue
    tuples=line.strip().split('\t')
    gameName=tuples[0]
    games[gameName]={}
    games[gameName]['vector']=[float(wc) for wc in tuples[1:]]
#read category file
for line in file('p2_table.txt'):
    tuples=line.strip().split('\t')
    gname=tuples[0]
    games[gname]['actual']=tuples[2]
#classification
catetories=['fighting','sports','rpg','arpg','racing','platform','action','fps']
for c in catetories:
    performance=process_category(c,games)
    print('Category: %s'%c)
    for score in performance:
        print(score),
    print(score.mean())