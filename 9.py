l=[]
file = open("C:\data.txt", "rt")
data = file.read()
words = data.split()
w=len(words)
l.append(w)
Counter=0
CoList = data.split("\n")
for i in CoList:
    if i:
        Counter += 1
l.append(Counter)
print(l)
