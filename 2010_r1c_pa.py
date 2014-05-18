'''
Created on 2014-3-19

@author: ezonghu
'''

def CountCross(lines):
    total = len(lines)
    Counter = 0
    for i in range(total-1):
        [CurrL, CurrR] = lines[i]
        for [NextL, NextR] in lines[i+1:]:
            if CurrL<NextL and CurrR>NextR:
                Counter += 1
            if CurrL>NextL and CurrR<NextR:
                Counter +=1
    return Counter
            

f=open('A-large-practice.in')
first_line = f.readline()
Cases = int(first_line)
CaseId = 0
for s in f:
    CaseId += 1
    lineNum = int(s)
    lines = []
    for l in f:
        lines.append([int(i) for i in l.split()])
        lineNum-=1
        if lineNum==0:
            break
    print( "Case #%d: %d" % (CaseId, CountCross(lines)))
f.close()