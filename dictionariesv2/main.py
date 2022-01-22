# Do not modify these lines
__winc_id__ = '00a4ab32f1024f5da525307a1959958e'
__human_name__ = 'dictionariesv2'

# Add your code after this line
# def create_passport(name, date_of_birth, place_of_birth, height, nationality, stamps):
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality,
        # "stamps": stamps
    }
    return passport

def add_stamp(passport, country):
    first_stamp = {"stamps": [country]}
    if country == passport["nationality"]:
        return passport
    else:
        if "stamps" not in passport:
            passport.update(first_stamp)
        if "stamps" in passport:
            if country not in passport["stamps"]:
                passport["stamps"].append(country)
    return passport

def add_biometric_data(passport, data_type, data_value, date_recorded):
    first_biometric = {"biometric": {data_type: {"date": date_recorded, "value": data_value}}}
    if "biometric" not in passport:
        passport.update(first_biometric)
    else:
        passport["biometric"][data_type] = {"date": date_recorded, "value": data_value}
    # if "biometric" in passport:
    #     # new_data_type = {data_type: {"date": date_recorded, "value": data_value}}
    #     if data_type not in passport["biometric"]:
    #         # passport["biometric"].update(new_data_type)
    #         passport["biometric"][data_type] = {"date": date_recorded, "value": data_value}
    #     if data_type in passport["biometric"]:
    #         # passport["biometric"].update(new_data_type)
    #         passport["biometric"][data_type] = {"date": date_recorded, "value": data_value}
    return passport

passport = create_passport("Anna Anna","2002-12-31", "London", 1.66, "Afghanistan")
# passport = create_passport("Anna Anna","2002-12-31", "London", 1.66, "Afghanistan", ["Albania"])
# print(create_passport("Anna Anna","2002-12-31", "London", 1.66, "Afghanistan"))
# print(create_passport("Anna Anna","2002-12-31", "London", 1.66, "Afghanistan", ["Albania"]))
# print(add_stamp(passport, "Algeria"))

fingerprint_data = {
    "left_pinky": "2378945",
    "left_ring": "2349081",
    "left_middle": "132890",
    "left_index": "9823234",
    "left_thumb": "0924131",
    "right_thumb": "6234923",
    "right_index": "13249734",
    "right_middle": "34023784",
    "right_ring": "12332538",
    "right_pinky": "32458970",
}

print(add_biometric_data(passport, "eye_color_left", "brown", "2022-05-22"))
print(add_biometric_data(passport, "eye_color_right", "blue", "2022-05-22"))
print(add_biometric_data(passport, "finger_prints", fingerprint_data, "2022-01-12"))