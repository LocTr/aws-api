import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Book')

def lambda_handler(event, context):
    try:
        result = table.put_item(Item={
        'id': str(uuid.uuid1()),
        'author': event['author'],
        'title': event['title']
        })
    except:
        return {
            'statusCode': 404,
            'body': 'Unexpected error'
        }
    return {
        'statusCode': 200,
        'body': 'book added'
    }
