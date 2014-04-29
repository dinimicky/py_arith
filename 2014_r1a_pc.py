'''
Created on 2014-4-26

@author: ezonghu
'''

def solve(N,a):
    return 'GOOD' if sum((a[i]+N-i-1)%N for i in range(N)) > 485000 else 'BAD'

def process():
    fn="C:\Users\ezonghu\Downloads\C-small-practice"
    fi=open(fn+'.in')
    fo=open(fn+'.out','w')
    first_line = fi.readline()
    Cases = int(first_line)
    CaseId = 0
  
    for l in fi:
        N = int(l.strip())
        a = [int(i) for i in fi.next().split()]
        res = solve(N, a)
        CaseId += 1
        Output = "Case #%d: %s" % (CaseId, res)
        print Output
        fo.write(Output+'\n')
        if Cases == CaseId:
            break
    fi.close()
    fo.close()

    
process()

# for i in range(1000,10000,1000):
#     print stat(i)