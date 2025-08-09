import pandas as pd
import numpy as np
import random
from tqdm import tqdm
from gensim.models import Word2Vec 
import matplotlib.pyplot as plt
%matplotlib inline 
from datetime import datetime
import math
import matplotlib.mlab as mlab
import datetime
import scipy
import scipy.stats as stats
import seaborn as sns
# import required libraries for clustering
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import cut_tree
def main():
    df = pd.read_excel('Online Retail.xlsx')
    df['InvoiceNo'].unique().tolist(),len(df['InvoiceNo'].unique())
    # check for missing values
    df.isnull().sum()
    # remove missing values
    df.dropna(inplace=True)

    # check for missing values
    df.isnull().sum()
    df['Quantity']=df['Quantity'].apply(lambda x:-x if x<0 else x)
    #扣除退貨筆數以及相對應買的次數
    df=df.drop_duplicates(['Description','InvoiceDate','Quantity'],keep=False)
    len(df)
    #確認是否已經沒有退貨筆數和相對應買的次數
    df=df.drop_duplicates(['Description','InvoiceDate','Quantity'],keep='last')
    len(df)
    df['Amount']=df.Quantity*df.UnitPrice
    df=df[~(df['Amount']<0)]
    len(df)
    #一年
    a=df.groupby("CustomerID").StockCode.count().to_frame()
    b=a.reset_index()
    b.columns=['CustomerID','buytime']
    b   #一年內購買次數大於等於2次的客戶
    b=b[b['buytime']>=2]    
    df=df[df['CustomerID'].isin(b['CustomerID'].tolist())]
    df=df.reset_index(drop=True)
    user_history=df.groupby("CustomerID").StockCode.unique().reset_index()
    user_history['number of items']=user_history['StockCode'].apply(lambda x:len(x))
    user_behavior=pd.merge(b,user_history)
    user_behavior
    from datetime import date

    #將timestamp轉成df可讀屬性
    df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'])
    L=['year','month','day']
    df=df.join(pd.concat([getattr(df['InvoiceDate'].dt,i).rename(i) for i in L],axis=1))
    #如果df合併的欄位資料型態不相同,就不能用+'/'+ 或 apply('/'.join,axis=1),必須用map處理不同資料型態
    user['Date']=user['year'].map(str)+'/'+user['month'].map(str)+'/'+user['day'].map(str)
    user.head()
    # user.head()
    user.to_csv('D:/論文/知識型推薦系統/用戶分析/user.csv')
if __name__ == "__main__":
    main()    # 讀取資料

