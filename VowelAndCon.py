value = input(str("Enter a later:  "))
var = "vowel" if value == 'a' or value == 'e' or value == 'i' or value == 'o' or value == 'u' else "consonant"
print(var)
print('a'.upper())
print('a'.lower())
print(type(value))
if type(value) is float:
    print("String")
else:
    print("Others")
