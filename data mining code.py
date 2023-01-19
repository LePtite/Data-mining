# -*- coding: utf-8 -*-
import math
import numpy
import pandas
import matplotlib.pylab as plt
import matplotlib.pyplot as plotting
df=pandas.read_csv('C:\deleteThisFolder\imports-85.data',header=None)
df.tail(10)
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-ofdoors","body-style", "drive-wheels","engine-location","wheel-base",
"length","width","height","curb-weight","engine-type", "num-of-cylinders", "engine-size","fuelsystem","bore","stroke","compression-ratio","horsepower", "peak-rpm","city-mpg","highwaympg","price"]
print("headers\n", headers)
df.columns=headers
df.head(9)
df.dropna(subset=["price"], axis=0)
df.columns
df.columns
df.dtypes
df.describe(include = "all")
df[['length','compression-ratio']].describe()
df.replace("?", numpy.nan, inplace = True)
df.head(5)
missing_data=df.isnull()
missing_data.head(5)
for column in missing_data.columns.values.tolist():
	print(column)
	print (missing_data[column].value_counts())
	print(" ")
avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
"Average of normalized-losses: ",avg_norm_loss
df["normalized-losses"].replace(numpy.nan, avg_norm_loss, inplace=True)
avg_bore=df['bore'].astype('float').mean(axis=0)
"Average of bore:", avg_bore
('Average of bore:', 3.3297512437810943)
df["bore"].replace(numpy.nan, avg_bore, inplace=True)
avg_stroke=df["stroke"].astype("float").mean(axis=0)
df["stroke"].replace(numpy.nan,avg_stroke , inplace=True)
avg_horsepower = df['horsepower'].astype('float').mean(axis=0)
"Average horsepower:", avg_horsepower
df['horsepower'].replace(numpy.nan, avg_horsepower, inplace=True)
"Average peak rpm:", avg_peakrpm
df['peak-rpm'].replace(numpy.nan, avg_peakrpm, inplace=True)
df['num-ofdoors'].value_counts()
df['num-ofdoors'].value_counts().idxmax()
df['num-ofdoors'].replace(numpy.nan, "four", inplace=True)
df.dropna(subset=["price"], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)
df.head()
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")
df['city-L/100km'] = 235/df["city-mpg"]
df['highway-L/100km'] = 235/df["highwaympg"]
df['length'] = df['length']/df['length'].max()
df['width'] = df['width']/df['width'].max()
df['height'] = df['height']/df['height'].max()
df["horsepower"]=df["horsepower"].astype(int, copy=True)
plotting.hist(df["horsepower"])
plotting.xlabel("horsepower")
plotting.ylabel("count")
plotting.title("horsepower bins")
bins = numpy.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
group_names = ['Low', 'Medium', 'High']
df['horsepower-binned'] = pandas.cut(df['horsepower'], bins, labels=group_names,include_lowest=True)
df[['horsepower','horsepower-binned']].head(20)
df["horsepower-binned"].value_counts()
plotting.bar(group_names, df["horsepower-binned"].value_counts())
plotting.xlabel("horsepower")
plotting.ylabel("count")
plotting.title("horsepower bins")
plotting.hist(df["horsepower"], bins = 3)
dummy_variable_1 = pandas.get_dummies(df["fuel-type"])
dummy_variable_1.head()
dummy_variable_1.rename(columns={'fuel-type-diesel':'gas', 'fuel-type-diesel':'diesel'},inplace=True) 
dummy_variable_1.head()
df=pandas.concat([df, dummy_variable_1], axis=1)
df.drop("fuel-type", axis = 1, inplace=True)
aspiration_variable = pandas.get_dummies(df["aspiration"])
aspiration_variable.rename(columns={'aspiration-std':'turbo', 'aspiration-std':'std'},inplace=True)
df=pandas.concat([df, aspiration_variable], axis=1)
df.drop("aspiration", axis = 1, inplace=True)
#Return to this
df.to_csv("C:\Users\K\Documents\IFT360")







