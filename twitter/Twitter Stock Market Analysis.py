import pandas as pd 
import datetime 
from datetime import date,timedelta
import plotly.graph_objects as go #grafik kütüphanesini dahil ettik (plotly)
import plotly.express as px # verilerimizi dinamik bir grafik üzerinde göstermek için pylotly.express kütüphanesini dahil ediyoruz
import plotly.io as pio 
pio.templates.default = "plotly_white"
tw = pd.read_csv("TWTR.csv")#datasetimizi okuduk
print(tw.head())
print(tw.info())#sütun başlıkları ve içerikleri hakkında bilgi için
print(tw.isnull().sum()) # sütunlarımızdaki boş değerlere bakmak için kullandık
tw = tw.dropna() # boş satırları siliyoruz
figure = go.Figure(data=[go.Candlestick(x=tw["Date"], open=tw["Open"],high=tw["High"],low=tw["Low"],close=tw["Close"])])
figure.update_layout(title = "Twitter Stock Prices Over the Years", xaxis_rangeslider_visible=False)
figure = px.bar(tw,x ="Date",y="Close",color="Close")
figure.update_xaxes(rangeslider_visible=True)
figure = px.bar(tw,x="Date",y="Close",color="Close")
figure.update_xaxes(rangeslider_visible=True)
figure.update_layout(title = "Twitter Stock Prices Over the Years", xaxis_rangeslider_visible=False)
figure.update_xaxes(rangeselector = dict(buttons=list([
            dict(count=1,label="1m",step ="month",stepmode="backward"),
            dict(count=6,label="6m",step ="month",stepmode="backward"),
            dict(count=3,label="3m",step ="month",stepmode="backward"),
            dict(count=1,label="1y",step ="year",stepmode="backward"),
            dict(count=2,label="2y",step ="year",stepmode="backward"),
            dict(step ="all")


])))#farklı zamanlardaki stok fiyatlarını analiz etmek için butonlar ekledik,belirli periyodları görebiliriz

#twitter timeline'daki hareketliliğe bakmak için
tw["Date"]= pd.to_datetime(tw["Date"],format='%Y-%m-%d')
tw['Year']=tw['Date'].dt.year
tw["Month"] = tw["Date"].dt.month
figure = px.line(tw, 
              x="Month", 
              y="Close", 
              color='Year', 
              title="Complete Timeline of Twitter")



figure.show()