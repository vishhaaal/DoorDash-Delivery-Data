import pandas as pd
import json
import boto3

s3 = boto3.client('s3')
sns = boto3.client('sns')
target_bucket = 'doordash-target-zn-gds-de'
sns_topic_arn = ''

def lambda_handler(event,context):
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        obj = s3.get_object(Bucket=bucket, Key=key)
        df = pd.read_json(obj['Body'])

    except: