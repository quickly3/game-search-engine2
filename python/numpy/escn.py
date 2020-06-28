import csv
import numpy as np


with open('escn.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    data = [data for data in csv_reader]

data_np = np.asarray(data)

print(data_np)
# np.savetxt('escn_new.csv', data_np, delimiter=',', fmt="%s")
