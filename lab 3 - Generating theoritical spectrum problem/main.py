E="LEQN"
# k = 3
peptieties = []
sumi = []
LengthOfE=len(E)

def mainApp():
    i=0
    StSum=[['0']]
    while True:
        StagePep,StageSum= ProcessStage(i)
        # print StagePep,StageSum
        i+=1
        peptieties.append(StagePep)
        StSum.append(StageSum)
        # sumi.extend(StageSum)
        if i>=LengthOfE:
            #return
            print peptieties
            StSumArranged = mergeAndArrangeLists(StSum)
            print StSumArranged
            return
        #back to loop

def mergeAndArrangeLists(mainlist):
    li=[]
    for m in range(0,len(mainlist)):
        li+=mainlist[m]
    return sorted(li,key=int)

def ProcessStage(StageID):
    k=3
    i = 0
    i= StageID+1
    stPep=[]
    peptieties=[]
    sumi = []
    while True:
        if k<=0:
            return stPep,sumi
        if i>len(E):
            p=str(E[StageID:len(E)])
            # print "mm",p
            p+=str(E[0:(i-len(E))])
            # print "hhh",p
            i+=1
            k-=1
            peptieties=stPep.append(p)
            sumi.append(str(calculateSm(p)))
            if k <= 0:
                return stPep, sumi
        else:
            p = E[StageID:i]
            # print p
            i += 1
            k -= 1
            peptieties = stPep.append(p)
            # print sumi
            sumi.append(str(calculateSm(p)))





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

mainApp()
# Test_getValue()
# Test_calculateSm()
