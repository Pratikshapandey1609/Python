start = int(input('Enter Start :---'))
stop = int(input('Enter stop :------'))

skip = int(input('Number you want to skip  :-----'))


for i in range(start , stop):
    if i  == skip:
        continue
    print(i)