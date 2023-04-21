import os
import pandas as pd
import boto3
from io import BytesIO

def upload_folder_to_s3(bucket_name, folder_path):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Iterate over the files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # Generate the S3 object key by appending the file path to the bucket name
            object_key = os.path.join(root, file_name).replace(folder_path, '').lstrip('/')

            # Upload the file to the S3 bucket
            s3.upload_file(os.path.join(root, file_name), bucket_name, object_key)

    print(f"All files from folder '{folder_path}' have been uploaded to S3 bucket '{bucket_name}'.")


def read_csv_from_s3(bucket_name, file_path):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Read the CSV file from S3 into a BytesIO object
    object = s3.get_object(Bucket=bucket_name, Key=file_path)
    body = object['Body'].read()
    csv_bytes = BytesIO(body)

    # Load the CSV data into a Pandas DataFrame
    df = pd.read_csv(csv_bytes)

    return df
