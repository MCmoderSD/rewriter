input = []

with open("input.txt", "r") as reader:
    for r in reader.readlines():
        input.append(r)

list1 = []

for one in input :
    whatWeNeed1 = one.replace("", "")
    list1.append(whatWeNeed1)

list2 = []

for two in list1 :
    whatWeNeed2 = two.replace("", "")
    list2.append(whatWeNeed2)

list3 = []

for three in list2 :
    whatWeNeed3 = three.replace("", "")
    list3.append(whatWeNeed3)

list4 = []

for four in list3 :
    whatWeNeed4 = four.replace("", "")
    list4.append(whatWeNeed4)

list5 = []

for five in list4 :
    whatWeNeed5 = five.replace("", "")
    list5.append(whatWeNeed5)

with open("output.txt", "w") as write:
    for w in list1:
        write.write(w)