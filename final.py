import s3_connector as s3
import pandas as pd


# Read in your dataframe
df = s3.read_csv_from_s3(
    '../dataset/test.csv')
data = s3.read_csv_from_s3("summary.csv")
# Define the start and end index
start_index = 0
end_index = int(df.shape[0])
print(end_index)
product_id=[]
product_len=[]
# Iterate through the rows in the specified range
for i in range(start_index, end_index):
    print(str(df.iloc[i]["PRODUCT_ID"])+"--- "+str(df.iloc[i]["PRODUCT_TYPE_ID"]) )
    filename = str(df.iloc[i]["PRODUCT_TYPE_ID"])+".csv"
    product_id.append(df.iloc[i]["PRODUCT_ID"])
    try:
        ind =(data.loc[data['group_id'] == filename].index[0])
        product_len.append(data.iloc[ind]["average"])
    except: 
        product_len.append(100)

frame = {'PRODUCT_ID': product_id,
         'PRODUCT_LENGTH': product_len}
# Creating Dataframe
result = pd.DataFrame(frame).reset_index(drop=True)

result.to_csv('submittion.csv')



# data = pd.read_csv("summary.csv")
# ind =(data.loc[data['group_id'] == "0.csv"].index[0])
# print(data.iloc[ind]["average"])