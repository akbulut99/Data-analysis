import numpy as np 
import pandas as pd 
from numpy.random import randn

def calculateMean(df):
 totalsum = df.sum().sum()  
 totalnum = df.size - df.isnull().sum().sum()
 return totalsum / totalnum

arr = np.array([[10,20,np.nan],[5,np.nan,np.nan],[21,np.nan,10]]) # 3x3 lük bir matrsi oluşturduk
df = pd.DataFrame(arr,index=["Index1","Index2","Index3"],columns=["Column1","Column2","Column3"])

print(df.fillna(value= calculateMean(df),inplace=True)) #inplace ile matrisimizi güncelledik
print(df)