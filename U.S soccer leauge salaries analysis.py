import pandas as pd 
soccer = pd.read_csv("mls-salaries-2017.csv") #veri setini okuyoruz
soccer.head(n=10) #ilk 10 veriyi getirdik
len(soccer)#kaç veri olduğunu buluruz
soccer["base_salary"].mean() #toplam maaş ortalaması verir
soccer["base_salary"].max() #max maaşı verir
soccer[soccer["guaranteed_compensation"].max()== soccer["guaranteed_compensation"]]
#veri setimizdeki en yüksek tazminata sahip sporcunun bilgilerini verir
soccer[soccer["last_name"]=="Gonzalez Pirez"]["position"].iloc[0]
#gonzalez pirez ismindeki oyuncunun pozisyon bilgisini verir
soccer.groupby("position").mean()#oyuncuları pozisyona göre gruplayın ortalama maaşlarını buluyoruz
soccer["position"].unique()#kaç farklı posizyon olduğunu gösterir




