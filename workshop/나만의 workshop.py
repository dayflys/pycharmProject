import numpy as np

from pandas import DataFrame

with open("./resourse/tourism.csv",'r',encoding='utf-8') as f:
    line = f.readline()

    lines = f.readlines()

    df = DataFrame(lines, columns=[line])
    print(df)



