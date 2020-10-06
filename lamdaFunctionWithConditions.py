x = 10
if x != 11:
    print("Not equal")
else:
    print("equal")

arr = [11, 12, 16, 41, 15, 9, 8, 0]

for t in arr:
    temp = lambda x: f"Correct number is = {x}" if x > 10 else f"wrong number is =  {x}"
    print(temp(t))
