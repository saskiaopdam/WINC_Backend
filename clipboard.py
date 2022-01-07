player_1 = "Gullit"
player_2 = "Van Basten"

goal_1 = 32
goal_2 = 54

scorers = player_1 + " " + str(goal_1), player_2 + " " + str(goal_2)
print(scorers)

report = f'{player_1} scored in the {goal_1}nd minute\n{player_2} scored in the {goal_2}th minute.'
print(report)
print()