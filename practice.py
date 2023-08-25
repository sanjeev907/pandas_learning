import pandas as pd

dict1 ={'Name':['Priyang', 'Aadhya', 'Krisha', 'Vedant', 'Parshv', 'Mittal', 'Archana'], 'Marks':[98,89,99,87,90,83,99],' Gender':['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female']}
var = pd.DataFrame(dict1)
# a = var.head(3) # if we want to display only 3 starting row the we use it 
# a = var.tail(3) #check last 3 Rows of dataset
# a = var.shape   # find the number of row and column in the dataset.
# a = var.info() # find all detail about the data frame
# a = var.isnull().sum(axis=0)               # check all null values from the dataframes
# a=  var.describe(include='all')              # get overall statics about the dataframe
# a = var['Gender'].unique() #get the unique values from Gender Column
# a = var['Gender'].nunique() #get the unique numbers from Gender Column
# a = var['Gender'].value_counts()  # Dispaly the count of unique values in Gender Column
# a = (var['Marks'] >= 90) &   (var['Marks'] >= 100)                # find the total number of students having marks between 90 and 100 Using Between Method
# a = var['Marks'].mean() # find the mean of marks or average of marks column
# a = sum(var['Marks'].between(90,100)) # find the marks between the 90 and 100
# a = var['Marks'].min() # find the min marks from the column
# a = var['Marks'].max() # find the max marks from the column
# a = var['Marks'].median() # find the medium of marks from the column
# print(a)

## Apply Method
# it work on define the function in pandas
# def marks(x):
    # print(x//2) # it print the 2 divide the column marks

# var['Marks'].apply(marks) # how to apply method use 
# # var['half_marks'] = var['Marks'].apply(marks) # in this how we add new column in exiting column 
# print(var)


# # a = var['Marks'].apply(lambda x:x//2) # how to use apply method in lambda function
# a = var['Name'].apply(len) # find out the string value of Name column
# print(a)

###Mapping function

# a = var['Gender'].map({'Male':1,'Female':0}) # it help change the value of male & female value in gender column
# print(a)

## Drop column from the dataframe

# a = var.drop(columns=['Marks'], axis=1)
# print(a)

# TO display the row and Column 

# # a = var.columns
# a = var.index
# print(a)


#  Sorting the data in ascending and descending order 

# a = var.sort_values(['Marks','Name'],ascending=False) 
# print(a)


# display the name of female students

a = [var['Marks']  == 'Female']
print(a)