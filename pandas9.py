import pandas as pd 
dataset = pd.read_csv("USvideos.csv")#csv formatındaki dosyayı okumamızı sağlar
newdateset1 = dataset.drop(["video_id","trending_date"],axis = 1) #video_id,trending_date columnlarını silidik 
newdateset1.to_csv("USvideos1.csv",index = False) #elde ettiğimiz date seti yeni bir csv dosyası olarak yazıyoruz
  
excelset = pd.read_excel("excelfile.xlsx") #excel dosyası olarak kaydettik
excelset["Column5"] = ["Mustafa","Murat","Coşkun","Udemy"]
excelset.to_excel("newexcelfile.xlsx ")
 
