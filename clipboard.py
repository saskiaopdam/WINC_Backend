player_1 = "Gullit"
player_2 = "Van Basten"

goal_1 = 32
goal_2 = 54

scorers = player_1 + " " + str(goal_1), player_2 + " " + str(goal_2)
print(scorers)

report = f'{player_1} scored in the {goal_1}nd minute\n{player_2} scored in the {goal_2}th minute.'
print(report)
print()


def unique_koala_facts(num):
    unique_koala_facts = []
    while len(unique_koala_facts) < num:
        koala_fact = random_koala_fact()
        if koala_fact not in unique_koala_facts:
            unique_koala_facts.append(koala_fact)
    # print(len(unique_koala_facts))
    return unique_koala_facts

#2
def num_joey_facts():
    joey_facts = []
    if "joey" in random_koala_fact():
        joey_facts.append(random_koala_fact())
    num_joey_facts = len(joey_facts)
    print(num_joey_facts)
    return num_joey_facts


from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

def unique_koala_facts(num):
    unique_koala_facts = []
    while len(unique_koala_facts) < num:
        koala_fact = random_koala_fact()
        if koala_fact not in unique_koala_facts:
            unique_koala_facts.append(koala_fact)
    # print(unique_koala_facts)
    return unique_koala_facts


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
# if __name__ == "__main__":
#     print(random_koala_fact())

    unique_koala_facts(5)