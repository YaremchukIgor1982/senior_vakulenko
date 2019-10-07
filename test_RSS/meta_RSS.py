from pprint import pprint

import pandas as pd
import requests
import xlrd

df = pd.read_excel("C:\\Users\Administrator\PycharmProjects\Scum\\test_RSS\RegencyShutterMetaData.xlsx")

d = {}
for i in df['name'].unique():
    d[i] = [{df['value1'][j]: df['value2'][j]} for j in df[df['name']==i].index]
    print(d[i])
