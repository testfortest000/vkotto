resfile = open("otto.csv", 'r', encoding='utf-8', errors='ignore')

for line in resfile:
    data = line.split("\t")