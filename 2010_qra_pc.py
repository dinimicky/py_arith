fp = open('C-large-practice.in')

first_line = True
CaseNum = 0

KeyMap = {"a":"2", "b":"22", "c":"222",
          "d":"3", "e":"33", "f":"333",
          "g":"4", "h":"44", "i":"444", 
          "j":"5", "k":"55", "l":"555",
          "m":"6", "n":"66", "o":"666",
          "p":"7", "q":"77", "r": "777", "s":"7777",
          "t":"8", "u":"88", "v":"888",
          "w":"9", "x":"99", "y":"999", "z":"9999",
          " ": "0"
          }
    

for line in fp:
    if first_line:
        CaseTotal = int(line)
        first_line = False
        continue
    
    CaseNum += 1
    print( 'Case #%d:' % CaseNum, end = ' ')
    PressStr = ""
    for i in range(len(line[:-1])):
        if i > 0:
            if KeyMap[line[i-1]][0] == KeyMap[line[i]][0]:
                PressStr += " "+KeyMap[line[i]]
            else:
                PressStr += KeyMap[line[i]]
        else:
            PressStr += KeyMap[line[i]]
    print( PressStr)