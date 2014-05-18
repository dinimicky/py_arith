fp = open('B-large-practice.in')

first_line = True
CaseNum = 0

for line in fp:
    if first_line:
        CaseTotal = int(line)
        first_line = False
        continue
    
    words = line.split()
    words.reverse()
    CaseNum += 1
    print( 'Case #%d: %s' % (CaseNum, ' '.join(words)))