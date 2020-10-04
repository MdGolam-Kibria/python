arr = ["java", "c++", "python pro", "dart", "dart", "dart"]
print(len(arr[2]))
arr2 = arr.copy()
print(arr2)
print("initial array =  ", arr)

arr.append("swift")

print("after adding one element = ", arr)
# get one element from an array
print(arr[-1])

arr.pop()  # delete last element of the array
print(arr)
arr.insert(len("c++"), "java script")
print(arr)
print(len("c++"))
print("c++" not in arr)
print("ok  = ", len(arr[2]))
arr3 = arr.copy()
print(arr3)

print(arr3.index("dart"))  # ekhane dart er position return korbe
print(arr3.count("dart"))  # dart likha ta arrray ta koiber ase seta return kore


