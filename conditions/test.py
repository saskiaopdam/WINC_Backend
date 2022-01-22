# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time, need_milking, location, season, tank_is_full, grass_is_long):    
    if location == "pasture" and time == "night" or location == "pasture" and weather == "rainy":
        return "take cows to cowshed"
    if need_milking and location == "cowshed":
        return "milk cows"
    if tank_is_full and location == "cowshed" and weather != ("sunny" or "windy"):
        return "fertilize pasture"
    if grass_is_long and season == "spring" and weather == "sunny" and location != "pasture":
        return "mow grass"

    if need_milking and location == "pasture":
        return "take cows to cowshed\nmilk cows\ntake cows back to pasture"
    if tank_is_full and location == "pasture":
        return "take cows to cowshed\nfertilize pasture\ntake cows back to pasture"
    if grass_is_long and location == "pasture":
        return "take cows to cowshed\nmow grass\ntake cows back to pasture"
    else:
        return "wait"

print(farm_action('rainy', 'night', False, 'pasture', 'winter', True, True)) #take cows to cowshed
print(farm_action('rainy', 'night', True, 'cowshed', 'winter', True, True)) #milk cows
print(farm_action('neutral', 'day', False, 'cowshed', 'spring', True, False)) #fertilize pasture
print(farm_action('sunny', 'day', False, 'cowshed', 'spring', True, True)) #mow grass
print(farm_action('sunny', 'day', True, 'pasture', 'spring', True, True)) #take cows to cowshed\nmilk cows\ntake cows back to pasture
print(farm_action('sunny', 'day', False, 'pasture', 'spring', True, True)) #take cows to cowshed\nfertilize pasture\ntake cows back to pasture
print(farm_action('sunny', 'day', False, 'pasture', 'spring', False, True)) #take cows to cowshed\nmow grass\ntake cows back to pasture
print(farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True)) #wait