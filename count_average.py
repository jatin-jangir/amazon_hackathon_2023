import pandas as pd
import os
import s3_connector as s3
import pandas as pd

directory = "../dataset_segregated/dataset/"
group_id = []
average = []
count = []
std = []
min = []
Q1= []
Q2 = []
Q3 = []
max = []
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        url = "https://amazon-hackathon-2023.s3.ap-south-1.amazonaws.com/dataset/"+filename
        print(filename)
        data = s3.read_csv_from_s3(url)
        desc = data.describe()
        group_id.append(filename)
        count.append(desc['PRODUCT_LENGTH']['count'])
        average.append(desc['PRODUCT_LENGTH']['mean'])
        std.append(desc['PRODUCT_LENGTH']['std'])
        min.append(desc['PRODUCT_LENGTH']['min'])
        Q1.append(desc['PRODUCT_LENGTH']['25%'])
        Q2.append(desc['PRODUCT_LENGTH']['50%'])
        Q3.append(desc['PRODUCT_LENGTH']['75%'])
        max.append(desc['PRODUCT_LENGTH']['max'])

# dictionary of lists
dict = {'group_id': group_id, 'average': average,'count': count, 'std': std, 'min': min, 'Q1': Q1, 'Q2': Q2, 'Q3': Q3,'max':max}

df = pd.DataFrame(dict)
print(df)
df.to_csv('summary.csv')
# url = "https://amazon-hackathon-2023.s3.ap-south-1.amazonaws.com/dataset/10426.csv"
# data = s3.read_csv_from_s3(url)
# desc=data.describe()
# print(desc)
# print(desc['PRODUCT_LENGTH']['count'])

