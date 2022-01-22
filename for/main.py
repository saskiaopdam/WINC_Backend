from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """
#1
def shortest_names(countries):
    def name_lengths(countries):
        name_lengths = []
        for country in countries:
            name_lengths.append(len(country))
        return name_lengths

    name_lengths = name_lengths(countries)

    shortest_length = min(name_lengths)
    shortest_names = []

    for country in countries:
        if len(country) == shortest_length:
            shortest_names.append(country)
    return shortest_names

#2
# def most_vowels(countries):
#     vowels = "aeiou"

#     leaderboard = [["", 0]]

#     for country in countries:
#         #count vowels
#         vowel_count = 0
#         for letter in country:
#             if letter.lower() in vowels:
#                 vowel_count += 1

#         #insert into leaderboard when deserving
#         for position in range(len(leaderboard)):
#             if vowel_count >= leaderboard[position][1]:
#                 leaderboard.insert(position, (country, vowel_count))
#                 break
#             if position > 2:
#                 break
        
#     return [x[0] for x in leaderboard[:3]]

def most_vowels(countries):
    def vowel_amounts(countries):
        vowel_amounts = []
        for country in countries:
            vowels_in_name = []
            for letter in country:
                if letter.lower() == "a":
                    vowels_in_name.append(letter)
                if letter.lower() == "e":
                    vowels_in_name.append(letter)
                if letter.lower() == "i":
                    vowels_in_name.append(letter)
                if letter.lower() == "o":
                    vowels_in_name.append(letter)
                if letter.lower() == "u":
                    vowels_in_name.append(letter)
            number_of_vowels = len(vowels_in_name)
            # print(vowels_in_name)
            # print(number_of_vowels)
            vowel_amounts.append(number_of_vowels)
        return vowel_amounts
    
    print(vowel_amounts(countries))
    vowel_amounts = vowel_amounts(countries)

    highest_amount = max(vowel_amounts)
    print(highest_amount)

    most_vowels = []
    
    for country in countries:
        vowels_in_name = []
        for letter in country:
            if letter.lower() == "a":
                vowels_in_name.append(letter)
            if letter.lower() == "e":
                vowels_in_name.append(letter)
            if letter.lower() == "i":
                vowels_in_name.append(letter)
            if letter.lower() == "o":
                vowels_in_name.append(letter)
            if letter.lower() == "u":
                vowels_in_name.append(letter)
        number_of_vowels = len(vowels_in_name)
        if number_of_vowels == highest_amount:
            most_vowels.append(country)
        if number_of_vowels == highest_amount-1:
            most_vowels.append(country)
        if number_of_vowels == highest_amount-2:
            most_vowels.append(country)
    
    print(most_vowels)
    # sorted = most_vowels.sort()
    return most_vowels

#3
def alphabet_set(countries):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    char_set = []
    country_set = []

    for country in countries:
        print(country[0])
        for char in country:
            if char.lower() in alphabet and char.lower() not in char_set:
                char_set.append(char)
                if country not in country_set:
                    country_set.append(country)
    print(len(alphabet))
    print(char_set) 
    print(country_set) 
    return country_set

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
    #1
    shortest_names(countries)

    #2
    most_vowels(countries)

    #3
    alphabet_set(countries)
    