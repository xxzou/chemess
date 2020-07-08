import os

all = os.listdir('../data/temp/good_mol2_v3.mdb')

subset_folder = os.listdir('../data/temp/subset')

subset = []
for folder in subset_folder:
    subset += os.listdir('../data/temp/subset/'+folder)
subset = list(set(subset))
for item in all:
    if item not in subset:
        print(item)
print(subset)