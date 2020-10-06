temp = round(12)
print(temp)
val = 12.3454657
print(round(val))  # return just a int value
print(round(val, 2))  # return what i want after dot
# now check a condition in python
logic = round(.2 + .3) == round(.5)
if logic:
    print("Your condition is true")
else:
    print("Your condition is false")
# another logic below
logic2 = round(.2 + .3, 5) == round(.5, 5)
if logic2:
    print(f"your condition is {logic2}")
else:
    print(f"your condition is  = {logic2}")
# another one logic below

tricks1 = round(1.9999999, 5)
tricks2 = round(1.9999999, 6)
result = (tricks1, tricks2 == tricks1)
if result:
    print("true")
else:
    print("false")
