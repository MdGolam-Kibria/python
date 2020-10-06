dic = {
    "name": "Zara",
    "age": 18,
    "district": "naogaon"
}

print(dic["age"])
print(dic["name"].upper().capitalize())

if dic["district"].startswith("nk"):
    print("yes")
else:
    print("No")

# another logic
if dic["age"].__eq__("18"):
    dic["age"] = 90
    temp = dic["age"].__add__(10)
    print(f"ok {temp}")
else:
    print("empty")

print(dic.keys())
print(dic.items())
print("value %s" % dic.setdefault("age", None))

# update a dictionary
dic2 = {
    "name": "Kibria",
    "age": 25,
    "district": "Naogaon"
}
print(dic)
dic.update(dic2)
print(dic)
dic2.__setitem__("color", "white")
print(dic2)


