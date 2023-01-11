import numpy as np 
import pandas as pd 
from numpy.random import randn

df = pd.DataFrame(data= randn(3,3),index =["a","b","c"],columns=["sütun1","sütun2","sütun3"])
#dataframeler serilerin birleşmiş halidir
print(df("sütun2"))#2.sütuna karşılık gelen değerleri gösterir

 