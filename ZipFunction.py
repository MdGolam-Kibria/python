roll = [11, 12, 13, 14, 15]
name = ["golam kibria", "anika", "plabon", "raju", "zahangir"]
zipLogic = list(zip(roll, name))
print(zipLogic)

# another zip logic below
convertZiptolist = zip(roll, name);
toList = list(convertZiptolist)
print(toList)
for x in toList:
    print(x[0])
    print(x[1])
