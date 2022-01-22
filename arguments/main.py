# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# 1
def greet(name, greeting='Hello, <name>!'):
    correct_greeting = greeting.replace("<name>", name)
    return correct_greeting

print(greet("Doc"))
print(greet("Helen", "What's up, <name>!"))

# 2
def force(mass, body="earth"):
    if body.lower() == "sun":
        gravity = 274 
    if body.lower() == "jupiter":
        gravity = 24.92
    if body.lower() == "neptune":
        gravity = 11.15
    if body.lower() == "saturn":
        gravity = 10.44
    if body.lower() == "earth":
        gravity = 9.798
    if body.lower() == "uranus":
        gravity = 8.87
    if body.lower() == "venus":
        gravity = 8.87
    if body.lower() == "mars":
        gravity = 3.71
    if body.lower() == "mercury":
        gravity = 3.7
    if body.lower() == "moon":
        gravity = 1.62
    if body.lower() == "pluto":
        gravity = 0.58
        
    force_exerted = mass * round(gravity, 1)
    return force_exerted

print(force(3.4, "Sun"))

# 3
def pull(m1, m2, d):
    G = 6.674 * (10 ** -11)
    F = G * ((m1 * m2)/d ** 2)
    return F

print(pull(3.4, 5.6, 10.0))