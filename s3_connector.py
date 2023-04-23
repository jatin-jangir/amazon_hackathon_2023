
import pandas as pd
import os
import boto3


def upload_folder_to_s3(bucket_name, folder_path):

    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            print(filename)
            s3 = boto3.client('s3')
            s3.upload_file(folder_path+filename,
                           bucket_name, "dataset/"+filename)


def read_csv_from_s3(file_path):
   

    # Load the CSV data into a Pandas DataFrame
    df = pd.read_csv(file_path)

    return df

