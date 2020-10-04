temp = [1, 2, 3, 4, 5, 6]
# result = [expression,for userDefKey in itarableList]
result = [x * x for x in temp]
print(result)
# now another magic in list
temp2 = [1, 2, 3, 4, 5, 6]
result2 = [x for x in temp2 if x % 2 == 0]
print(result2)
