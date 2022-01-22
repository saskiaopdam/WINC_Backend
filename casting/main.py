# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

#1
leek_price = 2
print("Leek is " + str(leek_price) + " euro per kilo.")

#2
leek_order = "leek 4"
space = leek_order.find(" ")
number = leek_order[space + 1:]
amount = int(number)
sum_total = leek_price * amount
print(sum_total)

#
broccoli_price = 2.34
broccoli_order = "broccoli 1.6"
space = broccoli_order.find(" ")
amount = float(broccoli_order[space + 1:])
sum_total = broccoli_price * amount
print(str(amount) + "kg broccoli costs " + str(round(sum_total, 2)) + "e")