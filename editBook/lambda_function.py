import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Book')

def lambda_handler(event, context):
    response = table.scan()

    items = response['Items']
    
    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }
