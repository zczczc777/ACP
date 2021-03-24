from sklearn.externals import joblib
from sklearn import svm
import pandas as pd
import numpy as np
import itertools
from sklearn.model_selection import KFold  
from sklearn import svm
from sklearn.model_selection import train_test_split
import math
#from xgboost import XGBClassifier
from sklearn.neighbors import KNeighborsClassifier
import easy_excel
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import minmax_scale 
from sklearn.model_selection import *
import sklearn.ensemble
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import roc_curve, auc
import sys
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB  
import subprocess
from sklearn.utils import shuffle
import itertools
from sklearn.ensemble import GradientBoostingClassifier
import sys
from sklearn.feature_selection import  f_classif
import warnings
np.set_printoptions(threshold=np.inf)
path=""
inputname=sys.argv[1]
outputname=inputname.split('.')[0]
name1=inputname.split('.')[0]

path1=""
Predict_file=sys.argv[2]
outputname1=Predict_file.split('.')[0]
name=Predict_file.split('.')[0]

def performance(labelArr, predictArr):
    #labelArr[i] is actual value,predictArr[i] is predict value
    TP = 0.; TN = 0.; FP = 0.; FN = 0.
    for i in range(len(labelArr)):
        if labelArr[i] == 0 and predictArr[i] == 0:
            TP += 1.
        if labelArr[i] == 0 and predictArr[i] == 1:
            FN += 1.
        if labelArr[i] == 1 and predictArr[i] == 0:
            FP += 1.
        if labelArr[i] == 1 and predictArr[i] == 1:
            TN += 1.
    if (TP + FN)==0:
        SN=0
    else:
        SN = TP/(TP + FN) #Sensitivity = TP/P  and P = TP + FN
    if (FP+TN)==0:
        SP=0
    else:
        SP = TN/(FP + TN) #Specificity = TN/N  and N = TN + FP
    if (TP+FP)==0:
        precision=0
    else:
        precision=TP/(TP+FP)
    if (TP+FN)==0:
        recall=0
    else:
        recall=TP/(TP+FN)
    GM=math.sqrt(recall*SP)
    #MCC = (TP*TN-FP*FN)/math.sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))
    return precision,recall,SN,SP,GM,TP,TN,FP,FN

if __name__ == "__main__":
    modelpath=path+"csvmodel/"+outputname+".model"
    datapath=path+outputname1+".csv"
    datapath1 =path+"class.csv"
    clf = joblib.load(modelpath)
    Test_data = pd.read_csv(datapath, header=None, index_col=None)
    train_data1 = pd.read_csv(datapath1, header=None, index_col=None)
    Y=np.array(train_data1[:][0])
    #Y = list(map(lambda x: 0, xrange(len(Test_data) // 2)))
    #Y2 = list(map(lambda x: 1, xrange(len(Test_data) // 2)))
    #Y.extend(Y2)
    #Y = np.array(Y)
    #print Y
    #print len(Y)
    X = np.array(Test_data)
    X_predict=clf.predict(X)
    X_predict_proba=clf.predict_proba(X)
    #pprint X_predict_proba
    #print X_predict.T
    #print len(X_predict)
    pd.DataFrame(X_predict_proba[:,1]).to_csv(outputname1+'predict_proba.csv',header=None,index=False)
    pd.DataFrame(X_predict.T).to_csv(outputname1+'predict_probac.csv',header=None,index=False)
 #   ROC_AUC_area=metrics.roc_auc_score(Y,X_predict_proba[:,1])
    ACC=metrics.accuracy_score(Y,X_predict)
    precision, recall, SN, SP, GM, TP, TN, FP, FN = performance(Y, X_predict)
#    F1_Score=metrics.f1_score(Y, X_predict)
 #   F_measure=F1_Score
 #   MCC=metrics.matthews_corrcoef(Y, X_predict)
    pos=TP+FN
    neg=FP+TN

    print SN
    print SP
    print ACC
    savedata=[[[ACC,precision, recall,SN, SP, GM,TP,FN,FP,TN,pos,neg]]]    
 #   savedata=[[[ACC,precision, recall,SN, SP, GM,F_measure,F1_Score,MCC,ROC_AUC_area,TP,FN,FP,TN,pos,neg]]]
    easy_excel.save("RF",[str(X.shape[1])],savedata,'1RF'+'_Predict_'+name+'.xls')
