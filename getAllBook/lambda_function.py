import json
import boto3
import logging

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Book')
logging.getLogger().setLevel(logging.DEBUG)

def error_response(statusCode, body):
    logging.debug(event)
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
        response = table.scan()

        items = response['Items']
    
        return {
            'statusCode': 200,
            'body': json.dumps(items)
        }
    except:
        logging.critical(event)
        return error_response(404, 'Unexpected Error')
