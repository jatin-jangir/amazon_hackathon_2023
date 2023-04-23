# # import subprocess
# # import os

# # directory = "../dataset_segregated/dataset/"
# # for filename in os.listdir(directory):
# #     if filename.endswith('.csv'):
# #         curl_command = "curl https://amazon-hackathon-2023.s3.ap-south-1.amazonaws.com/dataset/"+filename
# #         result = subprocess.run(curl_command.split(),capture_output=True, text=True)

# #         # Check the output for any errors
# #         if result.stdout.startswith("<?xml version"):
# #             print(filename)
# import pandas as pd
# import subprocess
# import os
# import s3_connector as s3
# import pandas as pd

# directory = "../dataset_segregated/dataset/"
# group_id = []
# average = []
# count = []
# std = []
# min = []
# Q1 = []
# Q2 = []
# Q3 = []
# max = []
# url = "https://amazon-hackathon-2023.s3.ap-south-1.amazonaws.com/dataset/0.csv"
# data = s3.read_csv_from_s3(url)
# desc = data.describe()
# group_id.append("filename")
# count.append(desc['PRODUCT_LENGTH']['count'])
# average.append(desc['PRODUCT_LENGTH']['mean'])
# std.append(desc['PRODUCT_LENGTH']['std'])
# min.append(desc['PRODUCT_LENGTH']['min'])
# Q1.append(desc['PRODUCT_LENGTH']['25%'])
# Q2.append(desc['PRODUCT_LENGTH']['50%'])
# Q3.append(desc['PRODUCT_LENGTH']['75%'])
# max.append(desc['PRODUCT_LENGTH']['max'])
# print("group_id"+str(len(group_id)))
# print("average"+str(len(average)))
# print("count"+str(len(count)))
# print("std"+str(len(std)))
# # dictionary of lists
# dict = {'group_id': group_id, 'average': average, 'count': count,
#         'std': std, 'min': min, 'Q1': Q1, 'Q2': Q2, 'Q3': Q3, 'max': max}

# df = pd.DataFrame(dict)
# df.to_csv('summary.csv')
# import s3_connector as s3
# import string_matcher
# import pandas as pd
# data = s3.read_csv_from_s3(
#     "https://amazon-hackathon-2023-new.s3.ap-south-1.amazonaws.com/cluster/4555.csv")
# string="hii hello world"
# # Apply your function to each row of the dataframe and create a new column with the scores
# data['score'] = data.apply(lambda row: string_matcher.product_similarity(
#     row['keywords'], string), axis=1)
# # Sort the dataframe based on the score
# data = data.sort_values(by=['score'], ascending=False)
# print(data)
# print(data.iloc[0]["avg_length"])

import pandas as pd
df= pd.read_csv("submittion.csv", index_col=False)
df = df.iloc[:, 1:]
df.to_csv('submittion.csv', index=False)