import s3_connector as s3

bucket_name = 'my-s3-bucket'
folder_path = './dataset'

s3.upload_folder_to_s3(bucket_name, folder_path)
