import csv
 
filename = r"SavedCorpus.csv"
adatos = open(filename)

rdatos = csv.reader(adatos)
#for dato in rdatos:
 #   print(dato)
for dato in rdatos:
    print(dato)