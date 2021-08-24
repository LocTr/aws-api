import json
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Book')

def lambda_handler(event, context):
    try:
        response = table.delete_item(Key={
            'id': event['id'],
        })
    except KeyError:
        return {
            "statusCode": 404, 
            "message": 'book does not exist'
        }
    return {
        "statusCode": 200, 
        "message": 'book deleted'
    }