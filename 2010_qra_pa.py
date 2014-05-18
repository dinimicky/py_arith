'''
Created on 2014-3-10

@author: ezonghu
'''
'''
Created on 2014-3-10

@author: ezonghu
'''

fp = open('A-large-practice.in')

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
        Credit = int(line)
        continue
    if CaseLine == 1:
        CaseLine +=1
        ItemNum = int(line)
        continue
    if CaseLine == 2:
        CaseLine = 0
        Items = [int(i) for i in line.split()]
        for i in range(ItemNum-1):
            Rest = Credit - Items[i]
            if Rest in Items[i+1:]:
                print( "Case #%d: %d %d" % (CaseItem, i+1, Items[i+1:].index(Rest)+i+2))
                break
        continue 
