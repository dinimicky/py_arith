'''
Created on 2014-3-11

@author: ezonghu
'''
fp = open('A-small-practice.in')

first_line = True
CaseNum = 0
CaseItem = 0
CaseLine = 0
for line in fp:
    if first_line:
        CaseNum = int(line)
        first_line = False
        continue
    if CaseLine == 0:
        CaseLine +=1
        CaseItem +=1
        VectorNum = int(line)
        continue
    if CaseLine == 1:
        CaseLine +=1
        Vector1 = [int(i) for i in line.split()]
        Vector1.sort()
        continue
    if CaseLine == 2:
        CaseLine += 1
        Vector2 = [int(i) for i in line.split()]
        Vector2.sort(reverse=True)
        Sum = 0
        for i,j in zip(Vector1, Vector2):
            Sum += i*j
        print "Case #%d: %d" % (CaseItem, Sum)
