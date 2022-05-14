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