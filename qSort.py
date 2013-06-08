'''
Created on 2013-6-8

@author: Brilliant
'''
Seq=list()
Seq=range(1,100)+range(300,400)+range(200,300)
Seq.reverse()
LargeSeq=range(1,1000)+range( 3000, 4000)+range( 200, 3000)
def qsort(List=[]):
    if len(List)== 1 or len(List)== 0:
        return List
    else:
        Pivot=List[ 0]
        Upper=[]
        Lower=[]
        for Value in List[ 1:]:
            if Value > Pivot:
                Upper.append(Value)
            else:
                Lower.append(Value)
        return qsort(Lower)+[Pivot]+qsort(Upper)
       


print Seq
print qsort(Seq)
# print LargeSeq
# print qsort(LargeSeq)
       
  
