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
    
    for vowel_amount in vowel_amounts:
        if vowel_amount == highest_amount:
            most_vowels.append(vowel_amount)
        if vowel_amount == highest_amount-1:
            most_vowels.append(vowel_amount)
        if vowel_amount == highest_amount-2:
            most_vowels.append(vowel_amount)
    
    print(most_vowels)
    sorted = most_vowels.sort()
    return sorted