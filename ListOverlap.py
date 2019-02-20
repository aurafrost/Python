"""
Checks and returns numbers that are common between two given lists.
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print("List a contains: "+", ".join(str(n) for n in a))
print("List b contains: "+", ".join(str(n) for n in b))
maxNumA = max(a)
maxNumB = max(b)
if maxNumA > maxNumB:
    finalMax = maxNumA
elif maxNumB > maxNumA:
    finalMax = maxNumB
else: #if maxNumA==maxNumB
    finalMax = maxNumA

common = []
for x in range(1,finalMax):
    if (x in a and x in b):
        common.append(x)
print("The common numbers between a and b are: "+", ".join(str(n) for n in common))