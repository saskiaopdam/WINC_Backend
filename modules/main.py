import this
import time
import math
from datetime import datetime
import sys
from greet import supergreeting

# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
def wait(seconds):
    time.sleep(seconds)
wait(2)

def my_sin(float):
    return math.sin(float)
print(my_sin(3.4))

def iso_now():
    return datetime.now().strftime("%Y-%m-%dT%H:%M")
print(iso_now())

def platform():
    return sys.platform

print(platform())

def supergreeting_wrapper(name):
    return supergreeting(name)
print(supergreeting_wrapper("Bob"))
