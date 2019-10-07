import json
import re
from collections import OrderedDict
from pprint import pprint
import re
import pandas as pd


file_path = 'C:\\Users\Administrator\PycharmProjects\Scum\\test_RSS\RegencyShutterMetaData.xlsx'
df = pd.read_excel(file_path, encoding='utf-16')
for index, value in df.iterrows():
    pprint({"page":value['Web Page'],'url': value['Web Page URL'], "meta title":value['Meta Title'],
            'meta description': value['Meta Description']})

