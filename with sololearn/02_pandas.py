# pandas -- read and manipulate the data;
import pandas as pd
df = pd.read_csv('sample.csv')
# print(df.head())
# col=df['Product']
# print(col.head());
# small_col = df[['Product','Price']]
# print(small_col.head())
df['shirt']=df['Product']=="Shirt";
print(df.head())
