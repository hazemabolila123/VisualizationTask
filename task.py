#import packages#Relation between weight and acceleration per origin
g =sns.relplot(x="weight",y="acceleration",data=mpg,kind="scatter" , col ="origin" )
plt.xticks(rotation =90)
g.fig.suptitle("How weight affects acceleration",y=1.1)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Read the data set
mpg = pd.read_csv("E:/hazem/Technology/Data science/CAT/5-Data Visulization/task/auto-mpg.csv")
mpg.head(n=10)

#Getting inforamtion abuot the DataFrame
mpg.info()

#Discover model year Column
g =sns.countplot(x="model year",data=mpg)
g.set_title("Car Model Year")              
plt.show()

#Discover origin Column
g =sns.countplot(x="origin",data=mpg)
g.set_title("Origin") 
plt.show()

#Relation between weight and acceleration per origin
g =sns.relplot(x="weight",y="acceleration",data=mpg,kind="scatter" , col ="origin" )
g.fig.suptitle("How weight affects acceleration",y=1.1)
plt.show()

#Relation between horsepower and acceleration per origin
g= sns.relplot(x="horsepower",y="acceleration",data=mpg,kind="scatter" ,col ="origin",hue="cylinders")
sns.set_context("talk")
plt.xticks(rotation=90)
g.fig.suptitle("How horsepower affects acceleration",y=1.1)
plt.show()

#MPG per years
g = sns.relplot(x='model year', y="mpg" , data=mpg,kind="line" , ci=None)
g.fig.suptitle("mpg through years" , y=1.1 , x=.6)

#Acceleration per years
g = sns.relplot(x='model year', y="acceleration" , data=mpg,kind="line")
g.fig.suptitle("acceleartion through years" , y=1.1 , x=.6 )

#Mean of weights per years
g=sns.catplot(x="model year",y="weight",data=mpg,kind="point",join=False)
plt.xticks(rotation=90)
g.fig.suptitle("Weight through Years",y=1.1,x=.6)


#################################Summary#################################
#1-I begin with importing the packages i will use during the visulization
#2-Then read the file and knowing some information about the dataset i work on,like Knowing the datatypes of all columns and numbre of non values
#3-Then I tried to know more about (origin , model year) columns by using countplot
#and from the visulization, We know the most cars used in this dataset are from (origin : 1)(year : 73)
#4-Then I use scatterplot to know how the weight of the car affect (acceleration) per each orgin 
#5-Then I use scatterplot to know how the horsepower of the car affect (acceleration) per each orgin and how the difference in no of cylinders affects that
#6-Then I use lineplot to know how the incrasing in years affect (mpg) 
#7-Then I use lineplot to know how the incrasing in years affect (horsepower) in terms of mean
#8-Then I use pointplot to know how the incrasing in years affect (weights) in terms of mean 

