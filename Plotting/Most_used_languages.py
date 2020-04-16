from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import csv
import pandas as pd
plt.style.use("fivethirtyeight")

data = pd.read_csv('data.csv')

#setting all Responder_id to ids
ids = data['Responder_id']
language_input = data['LanguagesWorkedWith']


language_cnt = Counter()


for lang in language_input:
    language_cnt.update(lang.split(';'))

#print(language_cnt.most_common(15))

languages = []
popularity = []
for element in language_cnt.most_common(15):
    languages.append(element[0])
    popularity.append(element[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
plt.title("Most popular programing languages")
#plt.xlabel("Languages")
plt.xlabel("Users")
plt.tight_layout()

plt.show()