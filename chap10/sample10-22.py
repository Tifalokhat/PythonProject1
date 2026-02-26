import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_excel('JD手机销售数据.xlsx')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.figure(figsize=(10,6))
labels=df['商品名称']
y=df['北京出库销量']

plt.pie(y,labels=labels,autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title('2028年1月北京各手机品牌出库量占比图')
plt.show()