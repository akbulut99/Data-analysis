import numpy as np
import pandas as pd 
from numpy.random import rand
df = pd.DataFrame(rand(4,3),["A","B","C","D"], ["Column1","Column2","Column3"])
print(df)
print(df["Column1"] > 0)#numpylarda filtreleme işlemeni pandasda da yapabiliyoruz
