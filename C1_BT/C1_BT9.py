t = int(input("t = "))
h = t // 3600
m = (t % 3600) // 60
s = t % 60

print(f"{h} hour {m} min {s} sec")
