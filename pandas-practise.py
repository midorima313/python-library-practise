import pandas as pd 

# series in pandas
s1 = pd.Series([1,2,3,4,5])
print(type(s1))
print(s1)
print()
print("-------------------------------------------------------------------------")
print()

#dictionary to a series
s2 = pd.Series({"a":1 ,"b":2 ,"c":3 ,"d":4})
print(s2)
print()
print("-------------------------------------------------------------------------")
print()

#custom index
ref_index = [1,2,3,4]
ref_data = ["a","b","c","d"]
s3 = pd.Series(ref_data , index=ref_index)
print(s3)
print(s3[2])

#------------------------------------------------------------------------------------------

#Dataframe
#from dictionary
data = {'Name' : ['John' , 'Alice' , 'Bob'] , 'Age' : [25,30,45] , 'City' : ['New York' , 'Los Angeles' , 'Chicago']}
df1 = pd.DataFrame(data)
print(type(df1))
print(df1)
print()
print("-------------------------------------------------------------------------")
print()

#from list
data = ["Dip" , "Mad" , "Dut"]
index1 = [1,2,3]
df2 = pd.DataFrame(data , index= index1)
print(df2)
print()
print("-------------------------------------------------------------------------")
print()

data = ["remy" , "natasha" , "jada"]
df4 = pd.DataFrame(data)
print(df4)
print()
print("-------------------------------------------------------------------------")
print()

#empty dataframe
df3 = pd.DataFrame()
print(df3)
print()
print("-------------------------------------------------------------------------")
print()

#dataframe with two columns
data = {"Name" : ['n1','n2','n3'] , "Age" : [21,23,22]}
df5 = pd.DataFrame(data)
print(df5)
print()
print("-------------------------------------------------------------------------")
print()
index2 = ['x' , 'y' , 'z']
df6 = pd.DataFrame(data , index=index2)
print(df6)
print()
print("-------------------------------------------------------------------------")
print()

#custom column names
data = [["skrillex" , 4 ], ["zomboy",9] , ["kygo",11] , ["alan walker",23]] 
df7 = pd.DataFrame(data , columns=['Singer' , 'number'])
print(df7)
print()
print("-------------------------------------------------------------------------")
print()

#changing column names
df8 = df7.rename(columns={'number':'digit'})
print(df8)
print()
print("-------------------------------------------------------------------------")
print()

# get columns nad indexs
print("columns->" , df8.columns)
print("index->" , df8.index)
print()
print("-------------------------------------------------------------------------")
print()

# reading csv files in pandas
df9 = pd.read_csv(r"C:\Users\dipan\Downloads\mtcars2.csv")
print(df9)
print()
print("-------------------------------------------------------------------------")
print()

# get no of rows and column-> shape
print("shape->",df9.shape)
print()
print("-------------------------------------------------------------------------")
print()
#get total no of elements-> size
print("size->",df9.size)
print()
print("-------------------------------------------------------------------------")
print()
#get innfo about the datframe
print("info->" , df9.info())
print()
print("-------------------------------------------------------------------------")
print()
#get mean max std count 255 50% 75% statistical data 
print("describe->" , df9.describe())
print()
print("-------------------------------------------------------------------------")
print()
#count
print("count->",df9.count())
print()
print("-------------------------------------------------------------------------")
print()
#min
print("min->",df9.min())
print()
print("-------------------------------------------------------------------------")
print()
#max
print("max->",df9.max())
#mean
# print("mean->",df9.mean())

#tail and head function
print("tail function->",df9.tail())
print("head function ->",df9.head())
print()
print("-------------------------------------------------------------------------")
print()

#extract a column from the dataframe
print("collecting a single column->",df9['disp'])
print("type->",type(df9['disp']))
print()
print("-------------------------------------------------------------------------")
print()

#filling up NaN values in dataframe
print(df9.fillna(df9.qsec.mean())) 
print()
print("-------------------------------------------------------------------------")
print()

#dropping columns -> if inplace true -> permanent changes
print(df9.drop(columns=['vs' , 'am']).head(2))
print()
print("-------------------------------------------------------------------------")
print()

#slicing iloc and loc
data = { 'Name': ['Alice', 'Bob', 'Charlie' , 'Jack', 'Donald', 'Chris'], 'Age': [25, 30, 35, 41, 45, 28], 'City': ['New York', 'Los Angeles', 'Chicago', 'Illinois', 'Boston', 'Paulo Alto'] } 
df10 = pd.DataFrame(data)
print(df10)
print()
print("-------------------------------------------------------------------------")
print()

#iloc
print("iloc examples")
print(df10.iloc[0:2,0:2])
print()
print("-------------------------------------------------------------------------")
print()
print(df10.iloc[3:6,1:3])
print()
print("-------------------------------------------------------------------------")
print()
print(df10.iloc[3:6,[0,2]])
print()
print("-------------------------------------------------------------------------")
print()

#loc
print("loc examples")
print(df10.loc[0:3 ,'Name':'City']) # -> here it means from name column to city column(city column included)
print()
print("-------------------------------------------------------------------------")
print()
print(df10.loc[:,['Name' , 'City']]) # -> here i am selecting only specific columns Name and City
print()
print("-------------------------------------------------------------------------")
print()
print(df10.loc[:2,:'Age'])
print()
print("-------------------------------------------------------------------------")
print()

#replacing all the values of the column with 100
df10.Age = 100
print(df10)
print()
print("-------------------------------------------------------------------------")
print()

#adding new column to the dataframe
df10['class']=9
print(df10)
print()
print("-------------------------------------------------------------------------")
print()

#copying data from one column to another
print("before copying data->",df9.head())
print()
print("-------------------------------------------------------------------------")
print()
df9['am'] = df9['gear'] * 10
print("after copying->",df9.head())
print()
print("-------------------------------------------------------------------------")
print()

#sorting the values of a dataframe based on the values of a particular column
print(df9.sort_values(by='mpg')) #-> default ascending
print()
print("-------------------------------------------------------------------------")
print()
print(df9.sort_values(by='mpg' , ascending=False)) #-> ascennding false
print()
print("-------------------------------------------------------------------------")
print()

#sorting based on multiple column
print(df9.sort_values(by=["mpg" , "disp"] , ascending=False))
print()
print("-------------------------------------------------------------------------")
print()

#checking if the values of the column starts with a substring. As this is a string operation, its case-sensitive
print(df9['Unnamed: 1'].str.startswith('Merc'))
print()
print("-------------------------------------------------------------------------")
print()

#Filtering dataframe rows based on conditioning
print(df9[df9["Unnamed: 1"].str.startswith('Merc')])
print()
print("-------------------------------------------------------------------------")
print()

#Filtering rows for numerical numbers
print(df9[df9["cyl"] == 4])
print()
print("-------------------------------------------------------------------------")
print()

#conditional | and &
print(df9[(df9['cyl'] > 5) | (df9['gear'] > 4)])
print()
print("-------------------------------------------------------------------------")
print()

#iterations in a datafrme
for i in df9.columns:
    print(i)
print()
print("-------------------------------------------------------------------------")
print()

columns_not_object_type = []
for i in df9.columns:
    if df9[i].dtype != 'object':
        columns_not_object_type.append(i)
print(columns_not_object_type)
# this i can used for various purpose like
print()
print("-------------------------------------------------------------------------")
print()

#lets find mmean for each columns of the table which doesnot contain and string value
print(df9.loc[:,columns_not_object_type].mean())
#putting it all together
#The code first identifies which columns in the DataFrame df9 are 
#of a type other than object (typically numeric columns). 
#It then prints the names of these columns. Finally, it calculates and prints the 
#mean of each of these numeric columns.

