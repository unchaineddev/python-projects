import json
import re

import pandas as pd

json_file = "seo_data.json"
data_list = []

with open(json_file, 'r', encoding='utf-8') as file:
    documents = file.read()

pattern = '(?=value).*(?=)'
value = re.findall(pattern, documents)

my_li = [x[9:] for x in value]

str_to_dict = [json.loads(x[:-2]) for x in my_li]


for i in str_to_dict:
    json_data = json.loads(i)
    data_list.append(json_data)

df = pd.json_normalize(data_list)
df.to_csv("21nov.csv", index=False)
