import csv
import pandas as pd
import numpy as np
import sys


sys.__stdout__ = sys.stdout
df = pd.read_csv('review.csv', delimiter=",", encoding='utf-8')
print(df.head())

header_rows = []
##group = x.groupby('business_id')['text'].unique()
##framed = group[group.apply(lambda x: len(x)>1)]
##print(framed.head())
####framed.to_csv('Sorted_reviews_final.csv')
##print("Completed processing of the CSV file")
header_rows = ['business_id', 'reviews']

group = df.groupby('business_id')['text'].unique()
framed = group[group.apply(lambda x: len(x)>1)]
print(framed.head())
framed.to_csv('Sorted_reviews_final2.csv', header=header_rows)
print("Completed processing of the CSV file")
