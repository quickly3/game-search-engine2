import os 
 
docList = os.listdir('../../storage/csv')
docList.sort()  
 
for i in docList:
    print(i)

file = "./combine.txt"

fname = open(file, "w")
for i in docList:
    x = open ('../../storage/csv/{0}'.format(i),  "r")
    fname.write(x.read())
    x.close()
    
fname.close()