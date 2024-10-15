import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('test.xlsx')
print(df)
plt.rcParams['font.sans-serif']=['Simhei']
plt.figure(figsize=(10,5))
labels=df['name']
y=df['Beijing']
plt.pie(y,labels=labels,autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title('2024')
plt.show()