def mainApp():
    spectrum = [0,97,97,99,101,103,196,198,198,200,202,295,297,299,299,301,394,396,398,400,400,497]
    mersTempList,pepLength = getPepAndLength(spectrum)
    mersList = convertToLetters(mersTempList)
    mer=1
    peptideList=[[0]]
    peptideList.append(mersList)
    while mer < (pepLength):
        pepTempList = peptideList[mer]
        expandedList=expandList(pepTempList,peptideList[1])
        # print expandedList
        excludedList = excludeFromList(expandedList,spectrum)
        # print excludedList
        peptideList.append(excludedList)
        mer +=1
    print peptideList
    return



def getPepAndLength(templist):
    mersList= []
    mer=0
    while mer<len(templist):
        if templist[mer] <=186:
            mersList.append(templist[mer])
        mer +=1
    if mersList.__contains__(0): #remove 0 from the out spec
        mersList.remove(0)
    return list(set(mersList)),len(mersList)

def Test_getPepAndLength():
    sp=[0,97,97,99,101,103,196,198,198,200,202,295,297,299,299,301,394,396,398,400,400,497]
    print getPepAndLength(sp)


def getLinearPep(param):#param is str
    temp=[]
    temp.append(param)
    for i in range(0,len(param)):
        for j in range(i,len(param)+i):
            if j>len(param):
                break
            if j!=i  :
                # if not temp.__contains__(param[i:j]) :
                temp.append(param[i:j])
    return temp

def Test_getLiniearPep():
    p="ABC"
    print getLinearPep(p)
    p="PVP"
    print getLinearPep(p)



def excludeFromList(tempList,specList):
    i=0
    outList  = tempList
    while i <len(outList):
        linearPep = getLinearPep(tempList[i])
        sl = specList
        j=0
        while j<len(linearPep):
            s = calculateSm(linearPep[j])
            if s in sl:
                sl.remove(s)
                j+=1
            else:
                outList.remove(tempList[i])
                # i-=1
                break
        i+=1
    return outList


def Test_excludeFromList():
    l = ["PV","PT","PC","VP","VT","VC","TC","TV","TP","CP","CV","CT"]
#    spec=[0,97,97,99,101,103,196,198,198,200,202,295,299,301,394,396,398,400,400,497]
    spec=[0,97,97,99,101,103,196,198,198,200,202,295,297,299,299,301,394,396,398,400,400,497]
    initial = ["P","V","T","C"]
    # print excludeFromList(l, spec)
    out = expandList(excludeFromList(initial, spec),initial)
    # print out
    r = excludeFromList(out, spec)
    print r
    out = expandList(r,initial)
    # print out
    e = excludeFromList(out, spec)
    print e



def expandList(tempList,initialList):
    listLength = len(tempList)
    mylist = []
    i=0
    j=0
    esize = len(tempList[0])-1
    while i<listLength:
        j = 0
        while j<len(initialList):
            # if tempList[i][esize] != initialList[j]:
            m=tempList[i]+initialList[j]
            mylist.append(m)
            j+=1
        i+=1
    return mylist

def Test_expandList():
    tempList=["PV","PT","PC"]
    initial = ["P","V","T","C"]
    p= expandList(tempList,initial)
    print "-- Passed -- "


def calculateSm(location):
    s=0
    sumi=0
    l = len(location)
    for i in range(0,l):
        s= getValue(location[i])
        sumi += s
    return sumi

def Test_calculateSm():
    l = "MN"
    print calculateSm(l)


def getValue(m):
    table=[["G",57],["A",71],["S",87],["P",97],["V",99],["T",101],["C",103],["I",113],["L",113],["N",114],["D",115],["K",128],["Q",128],["E",129],["M",131],["H",137],["F",147],["R",156],["Y",163],["W",186]]
    for i in range(0,len(table)):
        if table[i][0] == m:
            return table[i][1]
def Test_getValue():
    m = "M"
    print getValue(m)

def getChar(m):
    table=[["G",57],["A",71],["S",87],["P",97],["V",99],["T",101],["C",103],["I",113],["L",113],["N",114],["D",115],["K",128],["Q",128],["E",129],["M",131],["H",137],["F",147],["R",156],["Y",163],["W",186]]
    for i in range(0,len(table)):
        if table[i][1] == m:
            return table[i][0]
def Test_getChar():
    m = 101
    print getChar(m)


def convertToLetters(mersTempList):
    out = []
    for i in range(0,(len(mersTempList))):
        out.extend(getChar(mersTempList[i]))
    return out

def Test_convertToLetters():
    a=[101,97]
    print convertToLetters(a)

# Test_expandList()
Test_excludeFromList()
# Test_getPepAndLength()
# Test_getChar()
# Test_convertToLetters()
# mainApp()
# Test_getLiniearPep()