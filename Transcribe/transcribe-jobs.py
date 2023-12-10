import boto3
from boto3 import client
import json
import os
from os import listdir
from os.path import isfile, join

numx = 'num3'
bucket_name = 'source-s3-488184881631'
input_prefix_name = 'test1/'
output_prefix_name = 'target/' + numx + '/'
region = 'us-west-2'

s3 = boto3.client('s3', region_name=region)
response = s3.list_objects_v2(Bucket=bucket_name, Prefix=input_prefix_name)
#print(response)
keys = [content['Key'] for content in response['Contents']]
#print(keys)

transcribe = boto3.client('transcribe')
keys = keys[1:]

for key in keys:
  print(key)

  filename = key.split('/')[-1].split('.')[0]

  job_name = f"your-job-name-{numx}-{filename}"

  print(job_name,'\n')
  response = transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': f's3://{bucket_name}/{key}'},
    MediaFormat='wav',
    LanguageCode='en-US',
    OutputBucketName='source-s3-488184881631',
    OutputKey=output_prefix_name 
  )
  #print("Job started!")