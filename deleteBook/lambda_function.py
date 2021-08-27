import boto3
import json
import logging
from botocore.exceptions import ClientError

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
        id = event['id']
        response = table.delete_item(
            Key={
            'id': id
            },
            ConditionExpression = 'attribute_exists(id)'
        )
        return success_response(200, 'Book deleted')
    except ClientError as e:  
        if e.response['Error']['Code']=='ConditionalCheckFailedException':
            return error_response(404, 'Book does not exist')
    except KeyError:
        return error_response(404, 'Invalid syntax')
    except:
        logging.critical(event)
        return error_response(404, 'Unexpected error')