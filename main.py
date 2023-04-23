import pandas as pd
import cluster_formation
import s3_connector as s3


# Read in your dataframe
df = s3.read_csv_from_s3('https://amazon-hackathon-2023-new.s3.ap-south-1.amazonaws.com/summary.csv')

# Define the start and end index
start_index = 532
end_index = 1000

# Iterate through the rows in the specified range
for i in range(start_index, end_index):
    filename = df.iloc[i]["group_id"]
    print(filename)
    cluster_formation.make_cluster(filename)
    # Do whatever you need to do with the row
