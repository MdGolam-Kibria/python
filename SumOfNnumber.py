# 1^2+2^2......n^2 calculate sum
userInput = int(input("Enter your Number = "))
sum2 = 0
for i in range(1, userInput + 1):
    print(i)
    sum2 += i * i

print(sum2)
