import pandas as pd
import json
import boto3

s3 = boto3.client('s3')
sns = boto3.client('sns')
target_bucket = 'doordash-target-zn-gds-de'
sns_topic_arn = 'arn:aws:sns:ap-south-1:423736870603:assignmer-gds-de'

def lambda_handler(event,context):
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        obj = s3.get_object(Bucket=bucket, Key=key)
        df = pd.read_json(obj['Body'])

        filtered_record_df = df[df['status'] == ["delivered"]]
        target_key = key.split('/')[-1]
        target_key = 'filtered_'+ target_key
        target_path = f'{target_bucket}/{target_key}'
        s3.put_object(Body = filtered_record_df.to_json(), Bucket = target_bucket, Key = target_key)

        sns.publish(TopicArn = sns_topic_arn, Message = 'Processing Successful')
        return {
            'statusCode' : 200,
            'body' : json.dumps('Processing Successful')
        }
    
    except Exception as e:
        sns.publish(TopicArn = sns_topic_arn, Message = f'Processing Failed: {str(e)}')
        return {
            'statusCode' : 500,
            'body' : json.dumps(f'Processing Failed: {str(e)}')
        }