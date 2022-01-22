# def main():
#     print(greet("Bob"))

# def greet(name):
#     return f'Hi, {name}!'

# if __name__ == '__main__':
#     main()

# def weather_report(day):
#     print(f'Here\'s the weather for {day}')

# weather_report("today")

def weather_report(day='today'):
    print(f'Here\'s the weather for {day}')

weather_report()

# def send_email(sender, to, cc, msg):
#     print(f'from: {sender}, to: {to}, cc: {cc}, msg: {msg}')

# send_email('bob@example.com', 'preeti@example.com', 'eric@example.com', 'Thanks for the cake!')

def send_email(sender='bob@example.com', to='preeti@example.com', cc='eric@example.com', msg='Thanks for the cake!'):
    print(f'from: {sender}, to: {to}, cc: {cc}, msg: {msg}')

send_email()