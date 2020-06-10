import csv
import numpy as np


with open('escn.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = [data for data in csv_reader]

data_np = np.asarray(data)
data_np = np.delete(data_np,0,0)
data_np = np.delete(data_np,[0,1,2,3,6,7,9],1)

np.savetxt('escn_new.csv', data_np, delimiter=',')