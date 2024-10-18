n = int(input("XXX = "))
str_n = str(n)

while len(str_n) < 3:
    str_n = '0' + str_n

print(f"X** = {str_n[-3]}")
print(f"*X* = {str_n[-2]}")
print(f"**X = {str_n[-1]}")
