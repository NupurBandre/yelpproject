import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import csv
import pandas as pd
import numpy as np


def business_id_fetch(file_path, busName):
    with open(file_path, 'r',encoding='utf-8') as f:
        readCSV = csv.reader(f, delimiter=',')
        for row in readCSV:
            if(row[1] == busName):
                return row[0]
            else:
                continue
            print("Business Not found")


def wordCloud_acc_to_business(path,bus_Name):
    review_combined = ""
    busID = ""
    busID = business_id_fetch("business_extract.csv", bus_Name)
    print(busID)
    with open(path,'r',encoding='utf-8') as f:
        readCSV = csv.reader(f, delimiter = ",")
        for row in readCSV:
            ##print(row)
            rowdata = row[2]
            if(rowdata == busID):
                review_combined = review_combined + row[5]
                print(row[5])
            else:
                continue
        plt.figure(figsize=(20,10))
        wordclouda = WordCloud(background_color='white', mode = "RGB", width = 2000, height=1500).generate(review_combined)
        plt.title("Wordcloud for " + bus_Name + " reviews")
        plt.imshow(wordclouda)
        plt.axis("off")
        plt.show()
    return ""

user_input = input('Enter the full name of the Business for which you want to create a wordcloud ===>  ')
wordCloud_acc_to_business("review_train.csv", user_input)
