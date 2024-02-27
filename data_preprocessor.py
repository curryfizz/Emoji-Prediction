import csv

filename = input()
filename+=".csv"


i=0
with open(filename, 'r') as csvfile:
    datareader = csv.reader(csvfile)
    filecontent = [row for row in datareader]
        
        
modified_rows = []
for row in filecontent:
    commas = len(row)
    if row[commas-1].isdigit()==False:
        continue
    if commas>2:
        i+=1
        sentence = ''
        for value in row[:-1]:
            value.replace(',','')
            sentence+=value
        new_value = [sentence, row[commas-1]]
        row = new_value
    modified_rows.append(row)

    

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(modified_rows)
