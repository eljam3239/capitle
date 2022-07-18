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
    return None


def is_correct(guess, answer):
    if guess == answer:
        return True
    else:
        return False

def get_guess_data(city_name):
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
    
