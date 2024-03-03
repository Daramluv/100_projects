import os

def is_leap(year):
    return year % 4 == 0 and (year %100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month -1]
should_continue = True
while should_continue:
    year = int(input("Enter a year: ")) 
    month = int(input("Enter a month: ")) 
    days = days_in_month(year, month)
    print(days)
    continue_try = input("Do you want to try agian? Y/N: ").lower()
    if continue_try == "n":
        should_continue = False
        os.system('cls' if os.name == 'nt' else 'clear')