# Rewriter

### You can exchange up to 5 times

list1 = []<br>
<br>
for one in input :<br>
whatWeNeed1 = one.replace("``search for``", "``exchange with``")<br>
list1.append(whatWeNeed1)<br>

list2 = []<br>
<br>
for two in list1 :<br>
    whatWeNeed2 = two.replace("``search for``", "``exchange with``")<br>
    list2.append(whatWeNeed2)<br>
<br>
list3 = []<br>
<br>
for three in list2 :<br>
    whatWeNeed3 = three.replace("``search for``", "``exchange with``")<br>
    list3.append(whatWeNeed3)<br>
<br>
list4 = []<br>
<br>
for four in list3 :<br>
    whatWeNeed4 = four.replace("``search for``", "``exchange with``")<br>
    list4.append(whatWeNeed4)<br>
<br>
list5 = []<br>
<br>
for five in list4 :<br>
    whatWeNeed5 = five.replace("``search for``", "``exchange with``")<br>
    list5.append(whatWeNeed5)<br>
<br>
with open("output.txt", "w") as write:<br>
    for w in ``list 1,2,3,4,5``:<br>
        write.write(w)<br>
