'''
Created on 2014-5-1

@author: ezonghu
'''

from operator import itemgetter
def sbv6(d,reverse=False):
    return sorted(d.iteritems(), key=itemgetter(1), reverse = reverse)

def MaxValueSpan(Vs):
    N = len(Vs)
    Spans = [0] * N
    Spans[0] = 1
    Stack = [0]
    
    for i in range(1, N):
        while (Stack != [] and Vs[Stack[0]]<Vs[i]):
            Stack.pop(0)
            
        Spans[i] = i + 1 if Stack == [] else i - Stack[0]
        
        Stack.insert(0, i)
    return Spans


def solve2(E,R,N,Vs):
    Spans = MaxValueSpan(Vs)
    SortedVs = sorted(enumerate(Vs), key = itemgetter(1), reverse=True)
    AfterActEng = [None]*(N+1)
    AfterActEng[-1] = E
    for i, _v in SortedVs:
        if AfterActEng[i] == None:
            AfterActEng[i] = 0
        s = Spans[i]
        InitEng = AfterActEng[i-s]
        
        TotalEng = min(InitEng+s*R, E)
        for j in range(i-1, i-s,-1):
            TotalEng = max(TotalEng - R, 0)
            AfterActEng[j] = TotalEng
            if TotalEng == 0:
                break


    SpendEng = []
    
    for i in range(len(AfterActEng)-1):
        SpendEng.append(min(E, AfterActEng[i-1]+R)-AfterActEng[i])
    return sum(e*v for e, v in zip(SpendEng,Vs))

def solve(E,R,N,Vs):
    CurrCost = {E:0}
    for v in Vs:
        NextCost = {}
        for e,c in CurrCost.iteritems():
            for i in xrange(R-1,e+1):
                NE = min(e-i+R, E)
                if NE not in NextCost:
                    NextCost[NE] = c + i * v
                    continue
                NextCost[NE] = max(c + i * v, NextCost[NE])
        CurrCost = NextCost
    return max(CurrCost.itervalues())

        
def test():
    print solve(5,1,5,[2,1,4,1,2])

def process():
    fn="C:\Users\ezonghu\Downloads\B-large-practice"
    fi=open(fn+'.in')
    fo=open(fn+'.out','w')
    first_line = fi.readline()
    Cases = int(first_line)
    CaseId = 0
  
    for l in fi:
        [E,R,N] = [int(i) for i in l.split()]
        Vs = [int(i) for i in fi.next().split()]
#         res = solve(E,R,N,Vs)
        res2 = solve2(E,R,N,Vs)
        CaseId += 1
        Output = "Case #%d: %s" % (CaseId, res2)
        print Output
        fo.write(Output+'\n')
        if Cases == CaseId:
            break
    fi.close()
    fo.close()

# print solve2(5,1,3, [3,1,2])
# print solve(5,1,3,[3,1,2])
# test()
process()