#importss
import math
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


def generateRNACondonTable():
    rna = []
    rnaCodon = open('RNA_codon_table.txt', 'r')
    for line in rnaCodon:
        rna.append([line[0:3],line[4:5]])
    return rna

#this will process a block and a piptude and see if they are similar or not
#its test function is Test_processBlock
def processBlock(block,peptide):
    for i in rnaCodonTable:
        if i[0]==block :
            if peptide == i[1]:
                return block
            else:
                return None
    return None

def Test_processBlock():
    print ("###########################")
    print ("####Test_processBlock###")
    print ("###########################")
    #case 1
    blk = "AUA"
    pep= "I"
    out = processBlock(blk,pep);
    #expected output
    expected = "AUA"
    if out == None :
        actual = "None"
    else:
        actual = out
    print "expected Out: "+expected
    print "actual = "+actual
    if expected==out :
        print("////////////////// PASSED ////////////////")
    else:
        print("#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/  Failed  /#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/")

    #case 2
    blk = "AUG"
    pep= "M"
    out = processBlock(blk,pep);
    #expected output
    expected = "AUG"
    if out == None :
        actual = "None"
    else:
        actual = out
    print "expected Out: "+expected
    print "actual = "+actual
    if expected==out :
        print("////////////////// PASSED ////////////////")

    #case 3
    blk = "GCC"
    pep= "A"
    out = processBlock(blk,pep);
    #expected output
    expected = "GCC"
    if out == None :
        actual = "None"
    else:
        actual = out
    print "expected Out: "+expected
    print "actual = "+actual
    if expected==out :
        print("////////////////// PASSED ////////////////")


#should return a block of codons that have index i
#index start from 0
#test function is Test_getBlock()
def getBlock(i,section):
    # return section[3*int(i) :3*(int(i)+1)]
    return section[i :(i+3)]

def Test_getBlock():
    print ("###########################")
    print ("####Test_getBlock###")
    print ("###########################")
    #case 1
    section = "ATGGCC"
    i = 0
    out = getBlock(i,section);
    #expected output
    expected = "ATG"
    print "expected Out: "+expected
    print "actual = "+out
    if expected==out :
        print("////////////////// PASSED ////////////////")
    else:
        print("#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/  Failed  /#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/")

    #case 2
    section = "ATGGCC"
    i = 1
    out = getBlock(i,section);
    #expected output
    expected = "GCC"
    print "expected Out: "+expected
    print "actual = "+out
    if expected==out :
        print("////////////////// PASSED ////////////////")

# this function should process the section
# return null if section fail / and the section if it matches
# its test function is Test_processSection
def processSection(section,peptide):
    i=0
    j=0
    s=""
    while True:
        blk = getBlock(j,section)
        pep = peptide[i]
        p= processBlock(block=blk,peptide=pep)
        # print pep,blk,section
        if(p==None):
            # print j,i
            # print pep,blk,section
            # print "NONON"
            return None
        else:
            # print p
            s+=p
            if((len(peptide)-1) == i):
                return s
            else:
                j=j+3
                i=i+1

def Test_processSection():
    print ("###########################")
    print ("####Test_processSection###")
    print ("###########################")
    #case 1
    sec = "AUGGCC"
    pep = "MA"
    out = processSection(section=sec,peptide=pep)
    expected = "AUGGCC"
    print expected ,">>", out
    if expected==out :
        print("////////////////// PASSED ////////////////")
    else:
        print("#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/  Failed  /#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/")

    #case 2
    sec = "GCCGCG"
    pep = "AA"
    out = processSection(section=sec,peptide=pep)
    expected = "GCCGCG"
    print expected,">>",out
    if expected==out :
        print("////////////////// PASSED ////////////////")
    else:
        print("#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/  Failed  /#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/")

#return the no of sections for the DNA
# test function is Test_getNoOfSections
def getNoOfSections(dna,peptideLen):
    return math.floor(len(dna)/3/peptideLen)

def Test_getNoOfSections():
    print ("###########################")
    print ("####Test_getNoOfSections")
    print ("###########################")
    print getNoOfSections("ABSASDASD",2),">>","1"
    print getNoOfSections("ABSASDASDASD",2),">>","2"
    print getNoOfSections("ABSASDASDASDE",2),">>","2"

#this function should return the length of section
# its test function  is Test_getSection
def getSection(i,dna,peptide):
    lengthOfSection = len(peptide)*3
    return dna[lengthOfSection*i:lengthOfSection*(i+1)]

def Test_getSection():
    print ("###########################")
    print ("####Test_getSection")
    print ("###########################")
    #case 1
    print getSection(0,"ABSASDASD","MA"),">>","ABSASD"
    print getSection(1,"ABSASDQQQQQQ","MA"),">>","QQQQQQ"
    print getSection(2,"AAAAAAQQQQQQSSSSSS","MA"),">>","SSSSSS"
    #another case should be added if the section doesn't exists

## this fuction should take the DNA and get a list for the peptides available in this DNA for certain protein
# test function is  Test_dnaProcessing
def dnaProcessing(dna,peptide):
    i=0
    OPepList = []
    prSec=""
    lp=len(peptide)
    n_sections = getNoOfSections(dna,lp)
    # print n_sections,lp
    if lp < 1 :
        return None
    else:
        # print "else"
        o=getSection(0,dna,peptide)
        prSec=processSection(o,peptide)
        # print "pp>>",prSec
        if prSec != None :
            OPepList.append(prSec)
        while True:
            i+=1
            if i>=n_sections:
                return OPepList
            else:
                section = getSection(i,dna,peptide)
                prSec = processSection(section,peptide)
                if(prSec != None):
                    OPepList.append(prSec)

def Test_dnaProcessing():
    print ("###########################")
    print ("####Test_dnaProcessing")
    print ("###########################")
    dna = "AUGGCCAUGGCCCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    protien = "MA"
    print dnaProcessing(dna=dna,peptide=protien)


# #### convDnaToRnaSequences(seq) Description :
#         this function replaces the "T" with 'U' in all the list sequences it receive
# test function Test_convDnaToSequences
def convDnaToRnaSequences(seq):
    return seq.replace("T","U")


def Test_convDnaToSequences():
    print ("###########################")
    print ("####Test_convDnaToSequences")
    print ("###########################")
    dna = "ATGGCCAUGGCCCCCAGAACTGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    expected = "AUGGCCAUGGCCCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    out= convDnaToRnaSequences(dna)
    print out
    if expected==out :
        print("////////////////// PASSED ////////////////")
    else:
        print("#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/  Failed  /#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/")


# #### PrepareSequences Function Description :
#     * this function takes "seq" as first arg ,and Protein as 2nd arg
#     * if we let the size of Protein is n then start generate 3*n sequences from the start from n-1,n,n+1
#     for all n>=1
# tested at Test_prepareSequences
def prepareSequences(seq,Protein):
    strSeq =[]
    for index in range(3*len(Protein)):
        strSeq.append(seq[index:])
    return strSeq

def Test_prepareSequences():
    print ("###########################")
    print ("####Test_prepareSequences")
    print ("###########################")
    seq="AUGGCCAUGGCCCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
    Protein="MA"
    out =[]
    print prepareSequences(seq , Protein)

# get the rcDNA from DNA
#test function is Test_getReverseComplement
def getReverseComplement(DNA):
    rcDNA = str(Seq(DNA, IUPAC.unambiguous_dna).reverse_complement())
    return rcDNA

def Test_getReverseComplement():
    print ("###########################")
    print ("####Test_getReverseComplement")
    print ("###########################")
    print "delayed test"


############### main
def runMain():
    dna = "ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA"
    protein="MA"
    rna = convDnaToRnaSequences(dna)
    rc= getReverseComplement(dna)
    rcRna= convDnaToRnaSequences(rc)
    # print rna,rc,rcRna
    s= prepareSequences(seq=rna,Protein=protein)
    rcS= prepareSequences(seq=rcRna,Protein=protein)
    # print s,rcS
    i=0
    print len(s)

    while True:
        sequence = s[i]
        # print sequence
        rcSequence = rcS[i]
        rcPepList = dnaProcessing(dna=rcSequence,peptide=protein)
        PepList =  dnaProcessing(dna=sequence,peptide=protein)
        if(len(PepList) != 0):
            print "From DNA >>",i," :",sequence
            print ">>",PepList

        if(len(rcPepList) != 0):
            print "From Reversed Complement DNA >>",i," :",rcSequence
            print ">>" ,rcPepList

        i+=1
        if(len(s)<= i ):
            return



#globlal variables
rnaCodonTable = generateRNACondonTable()
# Test_processBlock();
# Test_getBlock();
# Test_processSection();
# Test_getNoOfSections()
# Test_getSection()
# Test_dnaProcessing()
# Test_convDnaToSequences()
# Test_prepareSequences()
runMain()
