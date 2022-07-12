from numpy import equal
import answer
import pandas as pd

def is_valid_guess(guess):
    cities = pd.read_csv("canadacities.csv", nrows = 61)
    valid_cities = cities["city"].values
    if guess in valid_cities:
        return True
    else:
        return False


    

def guess():
    while True:
        try:
            user_guess = input("Please enter a guess: ")
        except ValueError:
            print("You have entered an invalid input. ")
            continue
        if is_valid_guess(user_guess) == False:
            print("That is not one of the 60 most populous cities in Canada, try again: ")
            continue
        else:
            #print("that is a permissable guess")
            #print(user_guess)
            break
    return user_guess


def is_correct(guess, answer):
    if guess == answer:
        return True
    else:
        return False

if __name__ == "__main__":
    test_answer = answer.answer().city_name
    print(test_answer)
    test_guess = guess()
    print(test_guess)
    print(is_correct(test_guess, test_answer))


    #test_guess = 
    #print(test.test())
    #cities = pd.read_csv("canadacities.csv", nrows = 61)
    #valid_
    #print(cities["city"].values)
    
