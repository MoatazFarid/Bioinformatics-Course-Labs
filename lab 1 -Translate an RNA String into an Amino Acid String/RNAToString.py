
"""
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

# reading the dataset and comparing with rna
dataset = open('dataset.txt','r')
d= dataset.read()

i=0
out = ""
while i<d.__len__():
    for r in rnaCodon:
        if r[0] == d[i:(i+3)]:
            out += str(r[1])
    i+=3

# printing output the Amino Acid String
print out