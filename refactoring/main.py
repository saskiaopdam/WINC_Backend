__winc_id__ = "9920545368b24a06babf1b57cee44171"
__human_name__ = "refactoring"


class Homeowner:
    def __init__(self, name, address, needs):
        self.name = name
        self.address = address
        self.needs = needs


class Specialist:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession


class Electrician(Specialist):
    pass


class Painter(Specialist):
    pass


class Plumber(Specialist):
    pass


alfred = Homeowner('Alfred Alfredson', 'Alfredslane 123',
                   ['painter', 'plumber'])
bert = Homeowner('Bert Bertson', 'Bertslane 231', ['plumber'])
candice = Homeowner('Candice Candicedottir', 'Candicelane 321', [
                    'electrician', 'painter'])

alice = Electrician('Alice Aliceville', 'electrician')
bob = Painter('Bob Bobsville', 'painter')
craig = Plumber('Craig Craigsville', 'plumber')

print(alice.profession)
print(bob.profession)
print(craig.profession)

# alice_name = "Alice Aliceville"
# alice_profession = "electrician"
# bob_name = "Bob Bobsville"
# bob_profession = "painter"
# craig_name = "Craig Craigsville"
# craig_profession = "plumber"

# alfred_name = "Alfred Alfredson"
# alfred_address = "Alfredslane 123"
# alfred_needs = ["painter", "plumber"]
# bert_name = "Bert Bertson"
# bert_address = "Bertslane 231"
# bert_needs = ["plumber"]
# candice_name = "Candice Candicedottir"
# candice_address = "Candicelane 312"
# candice_needs = ["electrician", "painter"]


def contracted_specialists(homeowner):
    fullname = homeowner.name
    gap_pos = fullname.find(" ")
    firstname = fullname[0:gap_pos]
    contracted_specialists = []
    for need in homeowner.needs:
        if need == "electrician":
            contracted_specialists.append(alice.name)
        elif need == "painter":
            contracted_specialists.append(bob.name)
        elif need == "plumber":
            contracted_specialists.append(craig.name)
    return f"{firstname}'s contracts: {contracted_specialists}"


print(contracted_specialists(alfred))
print(contracted_specialists(bert))
print(contracted_specialists(candice))
# alfred_contracts = []
# for need in alfred_needs:
#     if need == alice_profession:
#         alfred_contracts.append(alice_name)
#     elif need == bob_profession:
#         alfred_contracts.append(bob_name)
#     elif need == craig_profession:
#         alfred_contracts.append(craig_name)

# bert_contracts = []
# for need in bert_needs:
#     if need == alice_profession:
#         bert_contracts.append(alice_name)
#     elif need == bob_profession:
#         bert_contracts.append(bob_name)
#     elif need == craig_profession:
#         bert_contracts.append(craig_name)

# candice_contracts = []
# for need in candice_needs:
#     if need == alice_profession:
#         candice_contracts.append(alice_name)
#     elif need == bob_profession:
#         candice_contracts.append(bob_name)
#     elif need == craig_profession:
#         candice_contracts.append(craig_name)

# print("Alfred's contracts:", alfred_contracts)
# print("Bert's contracts:", bert_contracts)
# print("Candice's contracts:", candice_contracts)
