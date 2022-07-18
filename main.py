from numpy import equal
import answer
import pandas as pd
import numpy as np



def is_valid_guess(guess):
    cities = pd.read_csv("canadacities.csv", nrows = 61)
    valid_cities = cities["city"].values
    if guess in valid_cities:
        return True
    else:
        return False


    

def guess(answer):
    while True:
        try:
            user_guess = input("Please enter a guess: ")
        except ValueError:
            print("You have entered an invalid input. ")
            continue
        if is_valid_guess(user_guess) == False:
            print("That is not one of the 60 most populous cities in Canada, try again: ")
            continue
        elif is_correct(user_guess, answer) == False:
            print("That is a valid guess, but it is incorect, please try again.\nHINT: ")
            print(hint(user_guess, answer))
            continue
        else:
            print("YOU WIN!!!!!!!!!!!!!!")
            #print(user_guess)
            break
    return user_guess


def hint(user_guess, answer):
    """Return a string that tells the user about province, lat, lng and population.    
    user_guess: a string of a city name
    answer: an answer object 
    """
    popdiff = ['\u25b2', '\u25bc']
    provdiff = ['\u2705', '\u274c']
    latdiff = ['\u25b2', '\u25bc']
    lngdiff = ['\u276f', '\u276e']
    data = get_guess_data(user_guess)
    guesspop = data['population']
    guessprov = data["province_name"]
    guesslat = data["lat"]
    guesslng = data["lng"]
    if guesspop == answer.population:
        pop_diff = "Correct Population"
    elif guesspop<answer.population:
        pop_diff = popdiff[0]
    else:
        pop_diff = popdiff[1]

    if guessprov == answer.province:
        prov_diff = provdiff[0]
    else:
        prov_diff = provdiff[1]

    if guesslat == answer.lat:
        lat_diff = "Correct Latitude"
    elif guesslat<answer.lat:
        lat_diff = latdiff[0]
    else: 
        lat_diff = latdiff[1]
    
    if guesslng == answer.long:
        lng_diff = "Correct Longitutde"
    elif guesslng < answer.long:
        lng_diff = lngdiff[0]
    else: 
        lng_diff = lngdiff[1]

    print("HINTS: Province: "+prov_diff+" Population: "+ pop_diff+" Latitude: " + lat_diff + " Longitude: "+ lng_diff)
    #print(popdiff, provdiff, latdiff, lngdiff)
    #return None


def is_correct(guess, answer):
    """Compares the two"""
    if guess == answer:
        return True
    else:
        return False

def get_guess_data(city_name):
    """Gets a city's data from the dataset given a city name
    city_name: a string
    """
    cities = pd.read_csv("canadacities.csv", nrows = 61)
    city = city_name
    return cities.loc[cities["city"] == city]

def run():
    test_answer = answer.answer().city_name
    print(test_answer)
    test_guess = guess(test_answer)
    


if __name__ == "__main__":
    """
    test_answer = answer.answer().city_name
    print(test_answer)
    test_guess = guess()
    print(test_guess)
    print(is_correct(test_guess, test_answer))
    """
    run()
    #guess_data = get_guess_data("Guelph")
    #print(guess_data['province_name'])
    #SHOULD I MAKE AN OBJECT TO REPRESENT THE GUESSDATA, OR NAH
    


    #test_guess = 
    #print(test.test())
    #cities = pd.read_csv("canadacities.csv", nrows = 61)
    #valid_
    #print(cities["city"].values)
    
