import s3_connector as s3
import cluster_formation

# Read in your dataframe
df = s3.read_csv_from_s3('https://amazon-hackathon-2023-new.s3.ap-south-1.amazonaws.com/summary.csv')

# Define the start and end index
start_index = 7000
end_index = 10000
filenames=[]
# Iterate through the rows in the specified range
for i in range(start_index, end_index):
    filename = df.iloc[i]["group_id"]
    try:
        s3.read_csv_from_s3("https://amazon-hackathon-2023-new.s3.ap-south-1.amazonaws.com/cluster/"+filename)
    except:
        filenames.append(filename)
print(filenames)
    # Do whatever you need to do with the row
for filename in filenames:
    print(filename)
    cluster_formation.make_cluster(filename)
