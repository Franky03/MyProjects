import csv
import pandas as pd
# with open('./Udemy/WeatherPandas/weather_data.csv') as file:
#     data= csv.reader(file)
#     temp=[]
#     for row in data:
#         if row[1] != 'temp':
#             temp.append(int(row[1]))
            

#     print(temp)

data= pd.read_csv("./Udemy/WeatherPandas/weather_data.csv")
print(data)

data_dict= data.to_dict()
# print(data_dict)
# null= data['temp'].isna()
# print(null)
media= data['temp'].mean()
# print(round(media))
# max= data['temp'].max()
# print(max)
# print(data[data.temp== data.temp.max()])

monday= data[data.day=='Monday']
monday_temp= int(monday.temp)
new= (((9*monday_temp)+160)/5)
print(new)

#create a dataframe from scratch
data_dict= {'students': ['Anya', 'James', 'Angela'], 'scores': [76, 56, 65]}
df= pd.DataFrame(data_dict)
df.to_csv('new_data.csv')
