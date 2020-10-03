#Solar Women
#Pre-processing where we match whether the list of food and beverages from the melatonin list matches those of the food and beverages
#  that are available to astronauts at space station
#  We print a boolean to indicate whether it matches


#read melatonin levels list from Nutrition_animal, nutrition_nut, nutrition_plant data and combine into one pandas

import pandas as pd

nutri_nut = pd.read_csv("Nutrition_nut.csv", encoding = "ISO-8859-1")
nutri_animal = pd.read_csv("Nutrition_animal.csv", encoding = "ISO-8859-1")
nutri_plant = pd.read_csv("Nutrition_plant.csv", encoding = "ISO-8859-1")

csv_file_list = ["Nutrition_nut.csv", "Nutrition_animal.csv", "Nutrition_plant.csv"]


#three nutritious csv files into one pandas dataframe

'''
list_of_dataframes = []
for filename in csv_file_list:
    list_of_dataframes.append(pd.read_csv(filename, encoding ="ISO-8859-1" ))

nutri_df = pd.concat(list_of_dataframes)

print(nutri_df.head(2))
for col in nutri_df.columns:
    print(col)

nutri_df.to_csv("Full_Nutri.csv")
'''
#-----------Read nutrition list

df = pd.read_csv("Full_Nutri_2.csv", encoding = "ISO-8859-1")

print(df.head(5))

df = df[pd.notnull(df['Name'])]

#--read columns-
for col in df.columns:
    print(col)

#--save only the relevant columns
df = df[['Name', 'MT Value or Range ng/g or pg/mL']]
df.sort_values(by='MT Value or Range ng/g or pg/mL', ascending=False, na_position='first')

#print(df.head(5))
#print(df.describe())
df.to_csv("Nutri_df.csv")

#---------------read csv file from melatonin list
df2 = pd.read_csv("SpaceFoodNutrition_AppendixB.csv", encoding = "ISO-8859-1")
print(df2.head(2))
print(list(df2.columns))

#---match---

matchedList=[]

#for each food in the melatonin list
for food1 in df['Name']:
    #check if it's in the SpaceNutrition
    check=df2['Food'].str.contains(food1).any()
    matched=check,food1
    matchedList.append(matched)


print(matchedList)

#----save in df and into csv
dfMatched = pd.DataFrame(matchedList)
dfMatched.to_csv("Matched_df.csv")