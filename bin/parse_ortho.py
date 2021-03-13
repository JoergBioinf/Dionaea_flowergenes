# impoert libraray for Regular expressions
import re

# set global cutoffs to make sure that we have the same over alls files
padjCutoff = 0.01
logfoldCutoff = 1

### Forget this part s you already have the needed dictionaries :D
# Teo Results
# flowerGenesArath = {
#    "AT1G04360" : "0.0001"
#    }
arathDESEq2 = open("TeoResult.txt", "r")
for line in arathDESEq2:
    columns = re.split(",",line)
    geneName = columns[0]
    padj = columns[6]
    logfold = columns[2]
    if padj <= padjCutoff and logfold >= logfoldCutoff:
        flowergenesArath[geneName] = padj

close arathDESEq2


# Nazdar Results
rimFlowerGenes = {
    "Gene.93198__Cluster-77442.11__g.93198__m.93198" : 1
    }

#Readin the Orthogroups
# report all Orthogroups with
# - Arath Flower gene
# - Dionaea Flower + Rim gene
ortho = open("orthotest.tsv", "r") #Leylas Results! Change to Orthogropus.tsv
#read in the file line by line
for line in ortho:
    #split the line into columns cutting on <TAB>
    columns = re.split("\t", line)
    #extract the columns into meaningful variables
    orthogroupID = columns[0]
    arathlist = columns[3]
    # the genes of a species come as string with ', ' asspearator
    arathGenes = re.split(", ", arathlist)
    containsDiffArath = 0 # Helper Variable to keep track whether there is a fower gene
    for arathGene in arathGenes:
        if arathGene in flowerGenesArath: # need the real dictionary here
          containsDiffArath = 1
    if containsDiffArath:
        #print(orthogroupID + " cotains diff regulated arath gene")
        dionaealist = columns[17]
        dionaeaGenes = re.split(", ", dionaealist)
        # the following lines work only when we have the dionaea dictionaries
        for dionaeaGene in dionaeaGenes:
            if dionaeaGene in rimGenes:
                if dionaeaGene in flowerGene:
                    print("We found one! In Orthogroup: " + orthogroupID)
      
close ortho
