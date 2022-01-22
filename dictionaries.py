from itertools import product


student_ages = {
    'bob': 10,
    'sharon': 9,
    'eli': 10,
    'preeti': 11
}

print(student_ages['bob'])

product = {
    "name": "tofu",
    "price": 2,
    "producer": {
        "name": "Tofu Company Limited",
        "countr_of_origin": "France"
    },
}

print(product["producer"]["name"])

students = [
    {
        "name": "Ali",
        "family_name": "Khan",
        "skills": {
            "Python": "beginner",
            "JavaScript": "expert",
        },
        "certificates": [
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Data Analytics with Python",
                "date_of_completion": "",
            },
        ],
    },
    {
        "name": "Jessica",
        "family_name": "van Alphen",
        "skills": {
            "Python": "advanced beginner",
            "JavaScript": "beginner",
        },
        "certificates": [
            {
                "name": "Front-end Development",
                "date_of_completion": "",
            },
            {
                "name": "Back-end Development",
                "date_of_completion": "2022-01-17",
            },
            {
                "name": "Data Analytics with Python",
                "date_of_completion": "2020-01-17",
            },
        ],
    },
]

print(students[1]["skills"]["JavaScript"]) #beginner
print(students[0]["certificates"][0]["date_of_completion"]) #22-01-17



# Do not modify these lines
__winc_id__ = '00a4ab32f1024f5da525307a1959958e'
__human_name__ = 'dictionariesv2'

# Add your code after this line
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality
    }
    return passport



if __name__ == "__main__":
    countries = get_countries()

    # """ Write the calls to your functions here. """wincpy
    # #1
    print(create_passport("Anna Anna","2002-12-31", "London", 1.66, "Afghanistan"))