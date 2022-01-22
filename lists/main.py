# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

#1
def alphabetical_order(film_names):
    film_names.sort()
    return film_names

film_names = ["Because They're Young", "Mod Squad", "Wagon Train", "Gilligan's Island", "Bachelor Father", "Checkmate"]
print(alphabetical_order(film_names))

#2
def won_golden_globe(film_name):
    if film_name.lower == "fiddler on the roof":
        return True
    if film_name.lower() == "jaws":
        return True
    if film_name.lower() == "star wars":
        return True
    if film_name.lower() == "schindler's list":
        return True
    if film_name.lower() == "memoirs of a geisha":
        return True
    return False

print(won_golden_globe("jaws"))

#3
def remove_toto_albums(film_names):
    if "Fahrenheit" in film_names:
        film_names.remove("Fahrenheit")
    if "The Seventh One" in film_names:
        film_names.remove("The Seventh One")
    if "Toto XX" in film_names:
        film_names.remove("Toto XX")
    if "Falling in Between" in film_names:
        film_names.remove("Falling in Between")
    if "Toto XIV" in film_names:
        film_names.remove("Toto XIV")
    if "Old Is New" in film_names:
        film_names.remove("Old Is New")
    film_names.sort()
    return film_names

film_names = ["Because They're Young", "Mod Squad", "Wagon Train", "Gilligan's Island", "Bachelor Father", "Checkmate", "Fahrenheit", "The Seventh One", "Toto XX"]

print(remove_toto_albums(film_names))