
from pandas_datareader import data as web

import datetime
start = datetime.datetime(2019,1,1)
end   = datetime.datetime(2020,7,2)
f = web.DataReader("F",'google',start,end)
print(f)