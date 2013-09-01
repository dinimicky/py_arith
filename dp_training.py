'''
Created on 2013-8-1

@author: ezonghu
'''

# 2 Line
# each station Sn
# exchange line Tn
# get the fastest result

def getFastestResultFor2Line(L1, L2, C1, C2, S1, S2, T12, T21, n):
    if (C1[n] + S1[n+1]) > (C2[n] + T21[n]+S1[n+1]):
        C1.append(C2[n] + T21[n]+S1[n+1])
        L1.append(2)

    else:
        C1.append(C1[n] + S1[n+1])
        L1.append(1)

        
    if (C2[n] + S2[n+1]) > (C1[n] + S2[n+1]+T12[n]):
        C2.append(C1[n] + S2[n+1]+T12[n])
        L2.append(1)
    else:
        C2.append(C2[n] + S2[n+1])
        L2.append(2)



S1=[7,9,3,4,8,4]
S2=[8,5,6,4,5,7]
T12=[2,2,3,1,3,4]
T21=[4,2,1,2,2,1]
C1=[0]
C2=[0]
L1=[]
L2=[]
for i in range(len(S1)-1):
    getFastestResultFor2Line(L1, L2, C1, C2, S1, S2, T12, T21, i)
    
print C1, C2
print L1, L2
print sum(S2)
