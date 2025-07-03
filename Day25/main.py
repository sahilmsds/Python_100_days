import pandas as pd
# dt = pd.read_csv("weather_data.csv")
# # temp_list = dt['temp']
# # print(f"Average of Temperature: {temp_list.mean()}")
# # print(f"The maximum temperature here is {temp_list.max()}")
# # print(dt[dt['temp'] == dt['temp'].max()])
# monday = dt[dt['day'] == "Monday"]
# monday_temp_f_ = (monday['temp'] * 9/5) + 32
# print(f"The temperature of Monday was {monday_temp_f_} F")
data = pd.read_csv("Squirrel_Data.csv")
data1 = data['Primary Fur Color']
data2 = data1.value_counts()
# data2.to_csv("squirrel_count.csv")
data = pd.read_csv('squirrel_count.csv')
print(data)

