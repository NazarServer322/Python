import boto3
import pathlib
import io
aws_region = "eu-north-1"
s3_bucket_name = "itstepnazar322"

#create bucket 
s3_client = boto3.resource("s3", region_name=aws_region)
location = {'LocationConstraint': aws_region}
bucket = s3_client.create_bucket(
    Bucket=s3_bucket_name,
    CreateBucketConfiguration=location)
print("Amazon S3 bucket has been created")

#chec bucket
iterator = s3_client.buckets.all()
print("show list of buckets")
for bucket in iterator:
    print(f"--{bucket.name}")
local_file_path = "C:\\text.txt"



#upload file in bucket
s3_client = boto3.client("s3", region_name=aws_region)

local_file_path = "C:\\text.txt"

def upload_files(file_name, bucket, object_name=None, args=None):
    if object_name is None:
        object_name = pathlib.Path(file_name).name  
    s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=args)
    print(f"'{object_name}' has been uploaded to '{bucket}'")

upload_files(local_file_path, s3_bucket_name, "custom_name_in2_s3.txt")
#download file from bucket
s3_client = boto3.client("s3", region_name=aws_region)

s3_client.download_file(s3_bucket_name,"custom_name_in_s3.txt", r"C:\s3.txt")
print('S3 object download complete')
