import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
P = a + b + c
S = math.sqrt(P*((P-a)*(P-b)*(P-c)))

print(P)
print(S)
