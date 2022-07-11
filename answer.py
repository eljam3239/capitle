import random
from select import select
import pandas as pd

cities = pd.read_csv("canadacities.csv", nrows = 61)

#selects a row from the biggest canadian cities csv
def select_city():
    city_num = random.randint(1, 61)
    city_data = cities.iloc[city_num]
    #city = city_data.to_dict()
    #city = city["city"]
    return city_data

#gets a particular attribute of a line of the cities dataframe
def get_data(citydata, typ):
    data = citydata.to_dict()
    data = data[typ]
    return data


x = select_city()
print(x)

city_name = get_data(x, "city")
print(city_name)