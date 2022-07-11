import random
from select import select
import pandas as pd

cities = pd.read_csv("canadacities.csv", nrows = 61)

class answer:
    def __init__(self):
        self.city = select_city()
        self.city_name = get_data(self.city, "city")
        self.province = get_data(self.city, "province_name")
        self.population = get_data(self.city, "population")
        self.lat = get_data(self.city, "lat")
        self.long = get_data(self.city, "lng")
        return None
    def test(self):
        return self.city, self.city_name, self.province, self.population, self.lat, self.long


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


ans = answer()
print(ans.test())