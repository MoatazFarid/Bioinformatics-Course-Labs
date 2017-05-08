
"""
Question : http://rosalind.info/problems/ba4a/

Algorithm Steps
 1- Covert the RNA Codon table to a list [[key1,val1],[key2,val2],..]
 2- convert every key to a value and save it to a string
"""


#####Converting RNA Table to list like

def conv():
    rna = []
    rnaCodon = open('RNA_codon_table.txt', 'r')
    for line in rnaCodon:
        rna.append([line[0:3],line[4:5]])
    return rna

rnaCodon = conv() #getting the list of rna codon

def checkinCodon(arg):
    for i in rnaCodon:
        if i[0]==arg :
            return True
    return False

def workout(d):
    i=0
    out = ""
    while i<d.__len__():
        if(checkinCodon(d[i:(i+3)])):
            for r in rnaCodon:
                if r[0] == d[i:(i+3)]:
                    out += str(r[1])
            i+=3
        else:
            print "7amaada"
            return []


# reading the dataset and comparing with rna
dataset = open('dataset.txt','r')
d= dataset.read()

out = workout(d)
# printing output the Amino Acid String
print out
