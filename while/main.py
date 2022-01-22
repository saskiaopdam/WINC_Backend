from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

def unique_koala_facts(num):
    loops, max_loops = 0, 1000 #dit vergeten, resultaat: infinite loop
    facts = []
    while len(facts) < num:
        fact = random_koala_fact()
        if fact not in facts:
            facts.append(fact)
        if loops > max_loops: #dit vergeten, resultaat: infinite loop
            break
        loops += 1
    return facts

def num_joey_facts():
    # joey_facts = []
    # fact_count = 0
    # # joey_facts = []
    # while fact_count < 10:
    #     fact = random_koala_fact()
    #     # if fact not in facts:
    #     if "joey" in fact:
    #         joey_facts.append(fact)
    #     for i in joey_facts:
    #         if i == fact:
    #             fact_count += 1
    #         # if fact_count > 10:
    #         #     break
    # # for i in facts:
    # #     if "joey" in fact:
    # #         joey_facts.append(fact)   
    # return len(joey_facts)
    first_fact = random_koala_fact()
    times_seen_first_fact = 0
    num_joey_facts = 0
    unique_facts = []

    while times_seen_first_fact < 10:
        fact = random_koala_fact()
        if fact == first_fact:
            times_seen_first_fact += 1
        if fact not in unique_facts:
            unique_facts.append(fact)
            if "joey" in fact.lower():
                num_joey_facts +=1
    return num_joey_facts

# def koala_weight():
    # weight_fact = []
    # while len(weight_fact) < 10:
    #     fact = random_koala_fact()
    #     if "weight" in fact:
    #         weight_fact.append(fact)
    # return weight_fact
def koala_weight():
    fact = random_koala_fact()
    while "kg" not in fact.lower():
        fact = random_koala_fact()
    return int(fact.split("kg")[0].split(" ")[-1])

# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    # print(random_koala_fact())
    
    print(unique_koala_facts(10))
    print(num_joey_facts())
    print(koala_weight())