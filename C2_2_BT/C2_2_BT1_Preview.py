month = int(input("Month: "))

if month in(1, 3, 5, 7, 8, 10, 12):
    print(f"Month {month} is 31 days")
elif month in(4, 6, 9, 11):
    print(f"Month {month} is 30 days")
elif month == 2:
    print("Month 2 is 28 days (29 days in Leap Year)")
else:
    print("Error")
