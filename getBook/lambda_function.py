import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Book')

def lambda_handler(event, context):
    try:
        response = table.get_item(
          Key={
            'id': event["queryStringParameters"]['id'],
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps(response['Item']),
        }
    except : 
        return {
            'statusCode': 404,
            'body': 'Item not found'
        }
    return {
        'statusCode': 404,
        'body': 'Unexpected Error!'
    }
    