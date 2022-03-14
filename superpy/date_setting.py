# Imports
from datetime import date, timedelta

# Variables
today = date.today()
yesterday = today - timedelta(1)


def set_date(args):
    # sub-command function - executes "set_date" command
    set_backwards = args.direction == "backwards"
    set_forwards = args.direction == "forwards"
    num_days = args.num_days

    if set_backwards:
        adjusted_date = today - timedelta(num_days)
        print(
            f"OK\nThe current date ({today}) is now set backwards to {adjusted_date}.")
    if set_forwards:
        adjusted_date = today + timedelta(num_days)
        print(
            f"OK\nThe current date ({today}) is now set forwards to {adjusted_date}.")
