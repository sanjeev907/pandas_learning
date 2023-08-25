import pandas as pd 
# # b = [5,6,2,8]
# # b = (5,6,2,8)
# b = {"name":"sanjeev","subject":"Pandas","classes":"MCA","email":"Null"}
# # a = pd.Series(b,index=["a","b","c","d"],dtype="int",name="Python")#it helps to change the index and also change the datatypes and include the name of the data
# a = pd.Series(b)
# print(a)
# print(type(a))


#data frame in pandas 

# a = [1,2,3,4,5,6,7]
# d = {
#     "a":[1,2,3,4,5],
#     "b":[1,2,3,4,5]
# }
# var = pd.DataFrame(d, columns=["a"],index=["a","b","c","d","e"])
# print(var)
# print(type(var))
# print(var["a"][3])


# Arithmetic operations in pandas 

# var = pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
# var["C"] = var["A"] + var["B"]
# print(var)


# insert or delete the data in pandas

# var = pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
# # insert data 
# # var.insert(1,"D",[7,8,9,7])
# # #
# # print(var)

# # how to copy limited data from the variable

# # var["python"] = var["A"][:1]
# # print(var)

# # delete data 

# var.pop("B")
# print(var)



#How to create CSV file in pandas

# a = {"A":[1,2,3,4],"B":[5,6,7,8]}
# d = pd.DataFrame(a)
# 
# d.to_csv("demo.csv")  # create csv file  if we not the excel index then pass(index = False) while at the time of file create 
#  print(d)                    # and for header pass (header = [1,2])


# how to read the csv file  with the help of python 

# a = pd.read_csv("C:\\Users\\sanje\\Desktop\\Pandas learning\\test.csv",nrows=5) #nrow it is use for get the particular ow from the csv file 
# a = pd.read_csv("C:\\Users\\sanje\\Desktop\\Pandas learning\\test.csv",nrows=5,usecols=["Variable_name","Value"])# it is use for get columns from the csv file
# a = pd.read_csv("C:\\Users\\sanje\\Desktop\\Pandas learning\\test.csv",nrows=5,usecols=[0,1])# also get the column  with index
# a = pd.read_csv("C:\\Users\\sanje\\Desktop\\Pandas learning\\test.csv",skiprows=[0])# to skip the number of rows
# a = pd.read_csv("C:\\Users\\sanje\\Desktop\\Pandas learning\\test.csv",index_col=["Variable_name"])# index call (yade aap ke or column ko index bana chata hai to index call use kar ga)
# a = pd.read_csv("C:\\Users\\sanje\\Desktop\\Pandas learning\\test.csv",header=[444])# suppose muja kese heading ko header bana hai too header use karga 
# a = pd.read_csv("C:\\Users\\sanje\\Desktop\\Pandas learning\\test.csv",names=["col1"])# suppose muja kese heading ka naam change hai too header use karga 
# a = pd.read_csv("C:\\Users\\sanje\\Desktop\\Pandas learning\\test.csv",header = None, prefix = "Col")# suppose hara pass jo csv file hai usse ma heading nhi too hum 
# a = pd.read_csv("C:\\Users\\sanje\\Desktop\\Pandas learning\\test.csv",dtype={"Value":"float"}) # aar ap koe data int ma or aap usse fload ma float convert kar na chato ho too 
# print(a)




# pandas function 8 video

# a = pd.read_csv("C:\\Users\\sanje\\Desktop\\Pandas learning\\test.csv")
# a.index #to find out index in csv file
# a.columns #to find out th all columns in csv file
# a.describe()# to find out min,max,% or some operations to use find out only find out  numeric values
# a.head(2) # to get the data in the fix amount to use head functions it provide the 5 data from starting 
# a.tail() # to get the data in the fix amt from down to up to use tail function it provide 5 data by default from the down
# a[:1]# to get fix no. row data while using indexing or slicing 
# a.index.array# if we want to see the data in array form using this function
# a.to_numpy  # if want to convert the file in data into numpy data
# a.sort_index(axis=0,ascending=False)  # to sort the data the of csv file using this function axis=0 meaning working on the row axis 
# a["Username; Identifier;First name;Last name"][0] = "sanjeev"    #if we want to change the data of particular column using index number
# a.loc[1,"Username; Identifier;First name;Last name"] = "charan"  #same as #if we want to change the data of particular column using index number
# a.loc[[2,3],["Username; Identifier;First name;Last name"]] # if we  want to get the data to particular column then using this function
# a.loc[:,["Username; Identifier;First name;Last name"]] # if we want to get all data of this particular columns
# a.loc[[2,3]:]  # if we want to all the data of this row index data using this method
# a.iloc[0,1]  # it get the particular data from the particular column(1)index and row(0)index
# a.drop("security",axis=1)               # if we want to drop any row$columns from get the data using this method
# print(a)


# pandas handling missing data values  video 9 meaning that (suppose in csv file have some NAN values in some columns I want drop(delete) or fill these columns means that handling missing data)

#delete NaN value function
# csv_1 = pd.read_csv("C:\\Users\\sanje\\Desktop\\Pandas learning\\test.csv")
# a  = csv_1.dropna() # it help to delete the data which contain NAN values along with the row parameter axis= denotes for row 
# a  = csv_1.dropna(axis=1) #it help to delete the data which contain NAN values along with the column parameter axis=1 denotes for column
# a  = csv_1.dropna(how = "any") # suppose in csv file row contain all columns blank or NaN and delete that row using this method 
# a  = csv_1.dropna(how = "all") sames as line no. 103 
# a  = csv_1.dropna(subset=["values"]) # to delete one NaN along with particular column 
# a = csv_1.dropna(thresh=2) # to delete the NaN values and add some data inside those NaN values  
# print(a)

# fill data into NaN values

# csv_1 = pd.read_csv("C:\\Users\\sanje\\Desktop\\Pandas learning\\test.csv")
# # a = csv_1.fillna("pandas")# it help to fill data into all NaN columns 
# # a = csv_1.fillna({"values":"pythom"}) # to fill particular NaN columns
# # a = csv_1.fillna(method="ffill") #to the data with forward data
# # a = csv_1.fillna(method="bfill") #to the data with backward data 
# # a = csv_1.fillna(method="ffill",axis=0)  # fill data along with axis 
# # csv_1.fillna(11,inplace=True)
# a = csv_1.fillna("python", limit  = 2)
# print(a)    

#handing missing values (Replace and interpolate) functions video 10

# replace function is use to replace particular set data on run time 

# x = pd.read_csv("C:\\Users\\sanje\\Desktop\\Pandas learning\\test.csv")
# a = x.replace(to_replace=1,value=5)
# a = x.replace(to_replace="booker12;9012;Rachel;Booker",value="python")
# a = x.replace("[A-Za-z]","python",regex=True)
# a = x.replace(1,method="ffill")
# a = x.replace(1,method="bfill")
# a = x.replace(1,method="bfill",limit=2)
# x.replace(1,method="bfill",limit=2,inplace=True)
# print(x)


# interpolate functions it help to fill all data which have no data 

# a = x.interpolate() # it onl works on numeric values only some fuction in screenshot in pandas learning
# print(a)


# Merge of two excel files and two data frames   video 11

# x = pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]}) # note key always same while mergering two data frames valus
# y = pd.DataFrame({"A":[1,2,54,47],"B":[5,6,4,10]})
# # # z = pd.merge(x,y,on="A") # it show the unique data in both the frames 
# # # z = pd.merge(x,y,how="outer",indicator=True) # it left, inner, outer, cross,right 
# # z = pd.merge(x,y,left_index=True,right_index=True,suffixes=("name","id"))
# z = pd.concat([x,y])
# print(z)

# # concat it use for to merge two series

# s = pd.Series([5,6,2,8])
# d = pd.Series([1,2,3,4])
# a = pd.concat([s,d],axis=1)
# print(a)


# group by video 12 # it is use for formting the data in right format while we have bulk of data 

# x = pd.DataFrame({"Name":["a","b","c","d","c","a","c","a","b","b","a"],"s_1":[5,6,7,8,10,52,66,4,74,66,54],"s_2":[4,7,9,2,15,61,6,8,63,8,74]})
# a = x.groupby("Name") # to get all group by data                    
# for x,y in a:
#     print(x)
#     print(y)
#     a.get_group("a")  # to get single data of any value then use this
#     a.min()
#     a.max()

# list(a)


# how to join and append dataframes video 13

# x = pd.DataFrame({"A":[5,6,7,8]},index=["a","b","c","d"])
# y = pd.DataFrame({"B":[41,71,59,22]},index=["a","b","c","d"])
# a = y.join(x,how="right")
# # a = x.append(y)
# print(a)


#how to reshape the pandas file 

# 1. Pivot function
# 2. Melt function

# Melt function

# x = pd.DataFrame({"day":[1,2,3,4,5,6], "eng": [10,50,64,6,8,69], "math": [15,12,6,76,63,7]})
# a = pd.melt(x)  # it used for show the data in vrtical form not in hortizontal form
# print(a)

# pivot function


x = pd.DataFrame({"day":[1,2,3,4,5,6], "eng": [10,50,64,6,8,69], "math": [15,12,6,76,63,7]})
# a = pd.pivot(x,index="day",columns="eng")

a =pd.pivot_table(x,index="day",columns="eng",aggfunc="sum",margins=True)                                     #use for perform arthemetic operation
print(a)