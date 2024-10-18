from datetime import datetime

y = int(input("Year: "))
current_y = datetime.now().year

print(current_y - y)
