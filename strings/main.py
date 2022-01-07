# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# part one
player_0 = "Ruud Gullit"
player_1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

# scorers = player_0 + " " + str(goal_0), player_1 + " " + str(goal_1)
scorers = player_0 + " " + str(goal_0) + ", " + player_1 + " " + str(goal_1)
print(scorers)

report = f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute'
print(report)
print()


# part two
player = "Rinat Dasayev"
space = player.find(" ")
first_name = player[0:int(space)]
last_name = player[int(space)+1:]
last_name_len = len(last_name)
initial = first_name[0]
name_short = f'{initial}. {last_name}'
chant = f'{first_name}! ' * (len(first_name) - 1) + f'{first_name}!'
good_chant = chant[len(chant) - 1] != " "
print(first_name)
print(last_name)
print(last_name_len)
print(name_short)
print(chant)
print(2 != 3)
print(2 != 2)
print(good_chant)