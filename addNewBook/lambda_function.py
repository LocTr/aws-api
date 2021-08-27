import boto3
import uuid
import logging
import json


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Book')
logging.getLogger().setLevel(logging.DEBUG)

def error_response(statusCode, body):
    return {
        'statusCode': statusCode,
        'body': json.dumps(body)
    }
    
def success_response(statusCode, body):
    return {
        'statusCode': statusCode,
        'body': json.dumps(body)
    }

def lambda_handler(event, context):
    logging.debug(event)
    try:
        author = event['author']
        title = event['author']
        
        result = table.put_item(Item={
        'id': str(uuid.uuid1()),
        'author': author,
        'title': title
        })
        return success_response(200, 'Book added successfully')
    except KeyError:
        return error_response(404, 'Invalid Request')
    except:
        logging.critical(event)
        return error_response(404, 'Unexpected Error')
