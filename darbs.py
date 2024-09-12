from tests import Sieviete, Cilveks

cilveku_saraksts = []

for i in range(5):
    cilveku_saraksts.append(Sieviete("Anna", "blonda", i))

for sieviete in cilveku_saraksts: 
    if sieviete.age % 2 ==0:
        sieviete.mainit_dzimumu()

print ("--------------")
for sieviete in cilveku_saraksts:
    sieviete.bazarsPaSevi()

