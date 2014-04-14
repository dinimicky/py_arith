'''
Created on 2014-4-12

@author: ezonghu
'''
def solve(first_row_set, second_row_set):
    res = first_row_set & second_row_set
    l = len(res)
    if l == 1:
        return res.pop()
    if l > 1:
        return "Bad magician!"
    if l == 0:
        return "Volunteer cheated!"
        
    
f=open('C:\Users\ezonghu\Downloads\A-small-attempt1.in')

first_line = f.readline()
Cases = int(first_line)
CaseId = 0
Line=0
first_matrix = []
second_matrix = []
for l in f:
    

    if Line == 0:
        first_row = int(l)-1
    elif Line <=4:
        first_matrix.append(set([int(i) for i in l.split()]))
    elif Line == 5:
        second_row = int(l)-1
    elif Line <= 9:
        second_matrix.append(set([int(i) for i in l.split()]))
        
    
    Line += 1
    if Line == 10:
        CaseId += 1
        print "Case #%d:" % (CaseId), solve(first_matrix[first_row], second_matrix[second_row])
        
        Line = 0
        first_matrix = []
        second_matrix = []
        
    
    if Cases == CaseId:
        break
f.close()