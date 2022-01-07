# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line
broccoli = 2
leek = 2
potato = 3
brussel_sprout = 7

sum_one_each = float(broccoli + leek + potato + brussel_sprout) # 14
avg_price = sum_one_each/4 # 3.5

num_potatoes = 7
num_broccolis = 5
num_leeks = 2
num_brussel_sprouts = 10

sum_total = float((broccoli * num_broccolis) + (leek * num_leeks) + (potato * num_potatoes) + (brussel_sprout * num_brussel_sprouts)) # 10 + 4 + 21 + 70 = 105

discount_percentage = 30

discounted_sum_total = sum_total-(sum_total*discount_percentage/100) #73.5

# print(sum_one_each) # 14
# print(avg_price) # 3.5
# print(sum_total) # 105
print(discounted_sum_total) # 73.5