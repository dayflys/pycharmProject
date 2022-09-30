'''

    중첩 dict

    dict_value = {  key1 : {key1-1:value},
                    key2 : {key2-1:value},
                    key3 : {key3-1:value},
                    ...}
    key1, key2 ==> 컬럼명으로 지정됨
    key1-1, key2-1 ==> 인덱스 지정됨

'''

import pandas as pd
import numpy as np

dict_value = {'key1' : {'key1-1':[1,2,3]},
              'key2' : {'key2-1':[1,2,3]},
              'key3' : {'key3-1':[1,2,3]}
              }
df = pd.DataFrame(dict_value)
print(df)
'''
             key1       key2       key3
key1-1  [1, 2, 3]        NaN        NaN
key2-1        NaN  [1, 2, 3]        NaN
key3-1        NaN        NaN  [1, 2, 3]
'''

#응용
dict_value = {'Nevada': {2001:2.4,2002:2.9},
              'Ohio': {2001:1.7, 2002:3.6}}
df = pd.DataFrame(dict_value)
print(df)

'''
      Nevada  Ohio
2001     2.4   1.7
2002     2.9   3.6
'''