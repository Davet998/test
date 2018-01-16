# pandas
import pandas
df1=pandas.DataFrame([[2,4,6],[10,20,30]], columns=["Price","Age","Value"], index=["First","Second"])
print(df1)
print(dir(df1))
df2=pandas.DataFrame([{"Name":"John"},{"Name":"Fred"}])
#print(df2)
print(df1.mean())
print(df1.Price.max())
print(df1.Price.min())

import pandas
#df1 = pandas.read_csv("C:\\git\\test\\supermarkets.csv")   #, header=None)
#print(df1)

#df2 = pandas.read_csv("http://pythonhow.com/supermarkets.csv")   #, header=None)
#print(df2)

df3 = pandas.read_json("http://pythonhow.com/supermarkets.json")
print(df3)

import geopy
dir(geopy)
