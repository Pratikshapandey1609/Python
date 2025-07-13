profile = {
    "name" : "raju",
    "age"  : "22",
    "email" : "pmishra221@gmail.com"
}

for k in profile:
    print(k)  # fetch only keys here 

for keys in profile.values():
    print(list(keys))  # fetch only values here

for keys in profile.items():
    print(keys)

