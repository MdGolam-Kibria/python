def squire(a):
    return a * a


num = [1, 2, 3, 4, 5, 6]

result = list(map(squire, num))  # map complete
print(result)
# now works with filter
num2 = [1, 2, 3, 4, 5, 6]
result2 = list(filter(lambda a: a % 2 == 0, num2))  # below description
'''
ekhane num2 theke loop chalaya value ene ene a er moddhe pass kore condition check kore jegola
milbe na segula remove korbe
'''
print(result2)
