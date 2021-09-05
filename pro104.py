import csv
from collections import Counter
with open("SOCR-HeightWeight.csv", newline= "") as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)
newdata = []

for i in range(len(filedata)):
    weight = filedata[i][2]
    newdata.append(float(weight))
    
n = len(newdata)
total = 0
for x in newdata:
    total = total + x
mean = total/n

print(mean)

newdata.sort()

if n%2 == 0:
    m1 = float(newdata[n//2])
    m2 = float(newdata[n//2-1])
    median = (m1+m2)//2
else:
    median = float(newdata[n//2])
print(median)

data = Counter(newdata)
modedata = {"65-90":0, "90-115":0, "115-140":0, "140-165":0, "165-190":0}

for weight1, occurences in data.items():
    if 65<float(weight1)<90:
        modedata["65-90"] += occurences
    elif 90<float(weight1)<115:
        modedata["90-115"] += occurences
    elif 115<float(weight1)<140:
        modedata["115-140"] += occurences
    elif 140<float(weight1)<165:
        modedata["140-165"] += occurences
    else:
        modedata["165-190"] += occurences

moderange, modeoccurence = 0,0

for range, occurence in modedata.items():
    if occurence>modeoccurence:
        moderange, modeoccurence = [int(range.split("-")[0]),int(range.split("-")[1])],occurence

mode = float((moderange[0]+moderange[1])//2)

print(mode)