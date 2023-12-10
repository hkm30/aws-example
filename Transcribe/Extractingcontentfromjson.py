import boto3
import json
import os

numx = 'num3'
bucket_name = 'source-s3-xxxxxxxxx'
prefix_name = 'target/' + numx + '/'
region = 'us-west-2'

s3 = boto3.client('s3', region_name=region)
with open('/Users/hekangmi/Downloads/transcripts-out.txt', 'w') as f:
  for obj in s3.list_objects(Bucket=bucket_name, Delimiter='/', Prefix=prefix_name)['Contents']:

    if obj['Key'].endswith('.json'):

       filename = obj['Key']
       #print(filename)

       response = s3.get_object(Bucket=bucket_name, Key=filename)
       data = json.loads(response['Body'].read().decode('utf-8'))

       transcript = data['results']['transcripts'][0]['transcript']
       print(transcript)
       #f.write(filename + "\n" + transcript + "\n")
  f.close()


#with open('transcript-ouput.txt', 'w') as f:
#  f.write(transcript + "\n")


