month = int(input("Month: "))

month_names = {
    1: "January", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

if month in(1, 3, 5, 7, 8, 10, 12):
    print(f"{month_names[month]} is 31 days")
elif month in(4, 6, 9, 11):
    print(f"{month_names[month]} is 30 days")
elif month == 2:
    print("February is 28 days (29 days in Leap Year)")
else:
    print("Error")
