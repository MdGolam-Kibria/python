value = [11, 12, 13, 14, 14, 14, 45, 46]
temp = lambda x: x ** 2 if x != 0 else f"x equal = {0}"

temp2 = list(map(temp, value))  # for map result
print(f"map result = {temp2}")

for i in value:
    print(f"loop result = {temp(i)}")
