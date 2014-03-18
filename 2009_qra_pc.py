'''
Created on 2014-3-16

@author: ezonghu
'''
code_jam = "welcome to code jam"

Counter=0
def calculateSubStr(String, Target):
    if Target == "":
        global Counter
        Counter+=1
        return True
    if String == "":
        return False
    
    for i in xrange(len(String)-len(Target)):
        if String[i]==Target[0]:
            calculateSubStr(str(String[i+1:]),str(Target[1:]))

def initTarget(Target=code_jam):
    Dict = {}
    for i in xrange(len(Target)):
        Key = Target[i]
        if Key not in Dict:
            Dict[Key] = [i]
        else:
            Dict[Key].append(i)
           
    return Dict
           
def calculateStrQuantity(String, Dict):
    global code_jam
    Res = [ 0 for i in range(len(code_jam))]
    for c in String:
        if c == 'w':
            Res[ 0] += 1
            continue
        if c in Dict:
            for i in Dict[c]:
                Res[i]=Res[i]+Res[i-1]

                   
               
    return Res[-1]
                        

f=open('C-large-practice.in')
first_line = int(f.readline())
CaseId = 0
Dict = initTarget()

for l in f:
    CaseId += 1
#     calculateSubStr(l, code_jam)
#     print "Case #%d: %04d" % (CaseId, Counter)
    print "Case #%d: %04d" % (CaseId, calculateStrQuantity(l.strip(), Dict) % 10000)
      
    Counter=0


       

    