num = 1
tempSum = 0
while num <= 10:
    print(num)
    tempSum += num
    if num == 10:
        print("Break")
        break
    num += 1
print(tempSum)
